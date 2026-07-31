import json

def save(class_name, value):
    data = None
    with open("Relics-and-Ruins/save.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    data[class_name] = value
    with open("Relics-and-Ruins/save.json", "w", encoding="utf-8") as s:
        json.dump(data, s, indent=4)

def load(class_name):
    data = None
    with open("Relics-and-Ruins/save.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data[class_name]
