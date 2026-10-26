import pandas as pd

graded = pd.read_json("data/graded.jsonl", lines=True)
hand = pd.read_csv("data/hand_labels.csv")

merged = hand.merge(graded[["id", "model", "label"]], on=["id", "model"])
merged["agree"] = merged["my_label"].str.strip().str.lower() == merged["label"]

print(f"Judge agreed with you on {merged['agree'].sum()} of {len(merged)} ({merged['agree'].mean():.0%})")
print("\nDisagreements:")
print(merged[~merged["agree"]][["id", "model", "my_label", "label"]])