import pandas as pd

graded = pd.read_json("data/graded.jsonl", lines=True)
sample = graded.sample(n=30, random_state=42)
sample = sample[["id", "model", "type", "prompt", "response"]]
sample["my_label"] = ""
sample.to_csv("data/hand_labels.csv", index=False)
print("Now fill in my_label for all 30 rows in data/hand_labels.csv")