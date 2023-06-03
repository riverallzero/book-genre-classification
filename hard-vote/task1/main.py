import pandas as pd

df_1 = pd.read_csv("submission_xlmrobert-large_5.csv")
df_2 = pd.read_csv("submission_prompt_10.csv")
df_3 = pd.read_csv("submission_prompt.csv")
df_4 = pd.read_csv("submission_xlmrobert.csv")

df = pd.DataFrame()
df["id"] = df_1["id"]
df["label_1"] = df_1["label"]
df["label_2"] = df_2["label"]
df["label_3"] = df_3["label"]
df["label_4"] = df_4["label"]

df["label"] = df[["label_1", "label_2", "label_3", "label_4"]].apply(lambda x: x.value_counts().idxmax(), axis=1)
df[["id", "label"]].to_csv("../submit/submission_1.csv", index=False)
