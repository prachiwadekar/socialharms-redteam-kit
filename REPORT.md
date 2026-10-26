# Results

120 attack prompts and 24 honest prompts graded. 0 judge errors excluded.

## Attack success rate by tactic

| tactic          | claude-haiku-5-5   | claude-sonnet-5-5   |
|:----------------|:-------------------|:--------------------|
| direct_ask      | 0%                 | 0%                  |
| false_authority | 8%                 | 50%                 |
| fiction         | 42%                | 100%                |
| obfuscation     | 0%                 | 0%                  |
| roleplay        | 0%                 | 0%                  |

## Attack success rate by harm

| harm                | claude-haiku-5-5   | claude-sonnet-5-5   |
|:--------------------|:-------------------|:--------------------|
| doxxing             | 20%                | 30%                 |
| enforcement_evasion | 0%                 | 30%                 |
| harassment          | 0%                 | 20%                 |
| impersonation_scams | 20%                | 40%                 |
| influence_ops       | 10%                | 30%                 |
| misinfo_fabrication | 10%                | 30%                 |

## Over-refusal rate on honest questions

| model             | over_refused   |
|:------------------|:---------------|
| claude-haiku-5-5  | 0%             |
| claude-sonnet-5-5 | 0%             |
