import json


def save(content):
    with open("score.json", "w") as file:
        json.dump(content, file, indent=4)

def load():
    try:
        with open("score.json", "r") as file:
            content = json.load(file)
            return content
    except:
        return None