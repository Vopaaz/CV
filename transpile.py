import yaml

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


import json

if __name__ == "__main__":
    with open("experience.yml", "r", encoding="utf-8") as f:
        data = yaml.load(f, Loader=Loader)

    with open("experience.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, separators=(",", ": "), ensure_ascii=False)

