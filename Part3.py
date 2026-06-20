import json

with open("/home/anoynmous/Documents/Sentinel-File-Organizer/config.json", "r") as f:
    rules = json.load(f)
    print(rules)

def add_rule(new_rule):
    with open("/home/anoynmous/Documents/Sentinel-File-Organizer/config.json", "r") as f:
        rules = json.load(f)
    rules.append(new_rule)
    with open("/home/anoynmous/Documents/Sentinel-File-Organizer/config.json", "w") as f:
        json.dump(rules,f)

add_rule({"name": "Move Images", "file_type": ".png", "destination": "/home/anoynmous/Pictures"})
    