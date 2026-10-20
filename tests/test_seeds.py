import yaml


def load(path):
    with open(path) as f:
        return yaml.safe_load(f)


def test_every_seed_uses_a_known_harm():
    harm_ids = {harm["id"] for harm in load("taxonomy.yaml")["harms"]}
    seeds = load("seeds.yaml")
    for item in seeds["attacks"] + seeds["benign"]:
        assert item["harm"] in harm_ids