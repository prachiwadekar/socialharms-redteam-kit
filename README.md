# Social Harms Red-Team Kit

An automated red-teaming pipeline that tests how LLMs handle social media harms, and whether they over-refuse honest users, using a harm × tactic taxonomy, an LLM judge, and a scorecard.

**Start here:** the [one-page project overview](OVERVIEW.md) covers why I built it, how it works, design decisions, and limitations. Full results tables are in [REPORT.md](REPORT.md).

## Headline results

Tested on 60 attack prompts and 12 honest questions, across two Claude models:

- **Simple tricks failed completely.** Direct asks, role-play, and obfuscation succeeded 0% of the time on both models.
- **A plausible reason worked.** Fiction framing drew at least partial help from Sonnet in all 12 attempts, and full compliance in 5.
- **The more capable model was more susceptible:** about 30% attack success on Sonnet versus 10% on Haiku.
- **The judge agreed with my blind hand labels 90% of the time**, erring on the lenient side, so these rates are a floor.

## How it works

| Step | File | What it does |
| --- | --- | --- |
| 1 | `taxonomy.yaml` | Defines 6 social media harms (each with a boundary of what doesn't count) and 5 attack tactics |
| 2 | `seeds.yaml` | 12 seed attack requests and 12 honest questions, 2 of each per harm |
| 3 | `mutators.py` | One function per tactic that wraps a seed in that tactic |
| 4 | `build_dataset.py` | Combines seeds and mutators into 72 prompts |
| 5 | `run.py` | Sends every prompt to two models, with retries and resume |
| 6 | `judge.py` | A third model grades each answer: complied, partial, or refused |
| 7 | `sample.py`, `agreement.py` | Picks 30 answers for blind hand labeling and measures judge agreement |
| 8 | `report.py` | Produces the results tables in `REPORT.md` |

## Run it yourself

You'll need Python 3.10+ and an Anthropic API key.

```bash
git clone https://github.com/prachiwadekar/socialharms-redteam-kit.git
cd socialharms-redteam-kit
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
echo "ANTHROPIC_API_KEY=your-key-here" > .env
mkdir -p data

python build_dataset.py
python run.py
python judge.py
python sample.py        # then fill in my_label in data/hand_labels.csv
python agreement.py
python report.py
```

Run the tests with `python -m pytest`.

## Responsible data handling

Raw model responses stay in `data/` on my machine and are excluded from the repo by `.gitignore`. Only aggregate rates are published. Child safety, self-harm, violent extremism, and sexual content are deliberately out of scope.

---

Built by Prachi Wadekar. I used AI as a coding partner on this project and can walk through every line.
