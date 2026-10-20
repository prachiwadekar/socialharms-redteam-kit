import json
import os
import time

import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

TARGET_MODELS = ["claude-haiku-5-5", "claude-sonnet-5-5"]
DATASET = "data/dataset.jsonl"
RESULTS = "data/results.jsonl"

def load_jsonl(path):
    if not os.path.exists(path):
        return []
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def ask(model, prompt, retries=3):
    for attempt in range(retries):
        try:
            reply = client.messages.create(
                model=model,
                max_tokens=500,
                messages=[{"role": "user", "content": prompt}],
            )
            return "".join(block.text for block in reply.content if block.type == "text")
        except anthropic.APIError as error:
            wait = 2 ** attempt
            print(f"  error: {error}. Retrying in {wait}s")
            time.sleep(wait)
    return None

def main():
    prompts = load_jsonl(DATASET)
    done = {(r["id"], r["model"]) for r in load_jsonl(RESULTS)}

    with open(RESULTS, "a") as out:
        for model in TARGET_MODELS:
            for row in prompts:
                if (row["id"], model) in done:
                    continue
                print(f"{model} <- {row['id']}")
                response = ask(model, row["prompt"])
                if response is None:
                    print("  gave up; run again later to retry")
                    continue
                out.write(json.dumps({**row, "model": model, "response": response}) + "\n")
                out.flush()


if __name__ == "__main__":
    main()