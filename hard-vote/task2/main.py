import pandas as pd

df_1 = pd.read_csv("submission_xlmrobert_2_best.csv")
df_2 = pd.read_csv("submission_xlnet_3_best.csv")
df_3 = pd.read_csv("submission_xlmrobert-large_5.csv")

df = pd.DataFrame()
df["id"] = df_1["id"]
df["label_1"] = df_1["label"]
df["label_2"] = df_2["label"]
df["label_3"] = df_3["label"]

df["label"] = df[["label_1", "label_2", "label_3"]].apply(lambda x: x.value_counts().idxmax(), axis=1)
df[["id", "label"]].to_csv("../submit/submission_2.csv", index=False)
