import json
from pathlib import Path

ROOT = Path("Relics-and-Ruins")


def read_json(file_name):
    path = ROOT / file_name

    if not path.exists():
        return {}

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(file_name, data):
    path = ROOT / file_name

    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def save(file_name, key, value):
    data = read_json(file_name)
    data[key] = value
    write_json(file_name, data)


def load(file_name, key, default=None):
    data = read_json(file_name)
    return data.get(key, default)