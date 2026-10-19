import yaml

with open("taxonomy.yaml") as f:
    tax = yaml.safe_load(f)

    print(len(tax["harms"]), "harms x", len(tax["tactics"]), "tactics =", len(tax["harms"]) * len(tax["tactics"]), "test cells")
    for harm in tax["harms"]:
        print("-", harm["id"], "(", harm["severity"], ")")