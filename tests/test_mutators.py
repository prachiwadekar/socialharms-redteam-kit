import yaml
from mutators import MUTATORS, direct_ask, obfuscation


def test_direct_ask_returns_request_unchanged():
    assert direct_ask("hello") == "hello"


def test_obfuscation_swaps_letters():
    assert obfuscation("hate") == "h@t3"

def test_every_tactic_in_taxonomy_has_a_mutator():
    with open("taxonomy.yaml") as f:
        tax = yaml.safe_load(f)
    for tactic in tax["tactics"]:
        assert tactic["id"] in MUTATORS