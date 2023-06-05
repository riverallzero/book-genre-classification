import torch

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


caption_model_name = 'blip-large'
clip_model_name = 'ViT-L-14/openai'

import gradio as gr
from clip_interrogator import Config, Interrogator

config = Config()
config.clip_model_name = clip_model_name
config.caption_model_name = caption_model_name
ci = Interrogator(config)


def image_analysis(image):
    image = image.convert('RGB')
    image_features = ci.image_to_features(image)

    top_mediums = ci.mediums.rank(image_features, 5)
    top_artists = ci.artists.rank(image_features, 5)
    top_movements = ci.movements.rank(image_features, 5)
    top_trendings = ci.trendings.rank(image_features, 5)
    top_flavors = ci.flavors.rank(image_features, 5)

    medium_ranks = {medium: sim for medium, sim in zip(top_mediums, ci.similarities(image_features, top_mediums))}
    artist_ranks = {artist: sim for artist, sim in zip(top_artists, ci.similarities(image_features, top_artists))}
    movement_ranks = {movement: sim for movement, sim in
                      zip(top_movements, ci.similarities(image_features, top_movements))}
    trending_ranks = {trending: sim for trending, sim in
                      zip(top_trendings, ci.similarities(image_features, top_trendings))}
    flavor_ranks = {flavor: sim for flavor, sim in zip(top_flavors, ci.similarities(image_features, top_flavors))}

    return medium_ranks, artist_ranks, movement_ranks, trending_ranks, flavor_ranks


def image_to_prompt(image, mode):
    ci.config.chunk_size = 2048 if ci.config.clip_model_name == "ViT-L-14/openai" else 1024
    ci.config.flavor_intermediate_count = 2048 if ci.config.clip_model_name == "ViT-L-14/openai" else 1024
    image = image.convert('RGB')
    if mode == 'best':
        return ci.interrogate(image)
    elif mode == 'classic':
        return ci.interrogate_classic(image)
    elif mode == 'fast':
        return ci.interrogate_fast(image)
    elif mode == 'negative':
        return ci.interrogate_negative(image)


import csv
import os
from IPython.display import clear_output, display
from PIL import Image
from tqdm import tqdm
import glob
import pandas as pd


category = os.listdir(r"/jbnu-swuniv-ai/train")
category = [name for name in category if 'desc' not in name]
category = category[7:]
save_path = r"/jbnu-swuniv-ai/train"

for cate in tqdm(category):
  folder_path = rf"C:\code\book-genre-classification\jbnu-swuniv-ai\train\{cate}" #param {type:"string"}
  prompt_mode = 'fast' #param ["best","fast","classic","negative"]
  output_mode = 'desc.csv' #param ["desc.csv","rename"]
  max_filename_len = 128 #param {type:"integer"}


  def sanitize_for_filename(prompt: str, max_len: int) -> str:
      name = "".join(c for c in prompt if (c.isalnum() or c in ",._-! "))
      name = name.strip()[:(max_len-4)] # extra space for extension
      return name

  ci.config.quiet = True

  files = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.png')] if os.path.exists(folder_path) else []
  prompts = []
  for idx, file in enumerate(tqdm(files, desc='Generating prompts')):
      if idx > 0 and idx % 100 == 0:
          clear_output(wait=True)

      image = Image.open(os.path.join(folder_path, file)).convert('RGB')
      prompt = image_to_prompt(image, prompt_mode)
      prompts.append(prompt)

  if len(prompts):
      if output_mode == 'desc.csv':
          csv_path = os.path.join(save_path, f'desc_{cate}.csv')
          with open(csv_path, 'w', encoding='utf-8', newline='') as f:
              w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
              w.writerow(['image', 'prompt'])
              for file, prompt in zip(files, prompts):
                  w.writerow([file, prompt])
          print(f"\n\n\n\nGenerated {len(prompts)} prompts and saved to {csv_path}, enjoy!")
      else:
          print(f"\n\n\n\nGenerated {len(prompts)} prompts and renamed your files, enjoy!")
  else:
      print(f"Sorry, I couldn't find any images in {folder_path}")


# Concat csv
merged_data = pd.DataFrame()

for root, dirs, files in os.walk(save_path):
    for file in files:
        if file.startswith('desc') and file.endswith('.csv'):
            save_path = os.path.join(root, file)
            df = pd.read_csv(save_path)
            merged_data = pd.concat([merged_data, df])

merged_data.to_csv('jbnu-swuniv-ai/merged_desc.csv', index=False)