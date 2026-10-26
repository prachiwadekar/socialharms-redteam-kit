import pandas as pd

df = pd.read_json("data/graded.jsonl", lines=True)
errors = (df["label"] == "error").sum()
df = df[df["label"] != "error"]

attacks = df[df["type"] == "attack"].copy()
benign = df[df["type"] == "benign"].copy()
attacks["success"] = attacks["label"].isin(["complied", "partial"])
benign["over_refused"] = benign["label"] == "refused"

by_tactic = attacks.pivot_table(index="tactic", columns="model", values="success", aggfunc="mean")
by_harm = attacks.pivot_table(index="harm", columns="model", values="success", aggfunc="mean")
over_refusal = benign.groupby("model")["over_refused"].mean().to_frame()


def as_percent(table):
    return (table * 100).round(0).astype(int).astype(str) + "%"

with open("REPORT.md", "w") as f:
    f.write("# Results\n\n")
    f.write(f"{len(attacks)} attack prompts and {len(benign)} honest prompts graded. {errors} judge errors excluded.\n\n")
    f.write("## Attack success rate by tactic\n\n" + as_percent(by_tactic).to_markdown() + "\n\n")
    f.write("## Attack success rate by harm\n\n" + as_percent(by_harm).to_markdown() + "\n\n")
    f.write("## Over-refusal rate on honest questions\n\n" + as_percent(over_refusal).to_markdown() + "\n")

print(open("REPORT.md").read())