import json


def save(content):
    """It gets the score number and saves it."""
    with open("score.json", "w") as file:
        json.dump(content, file, indent=4)

def load():
    """If something was saved before, it reads and returns it"""
    try:
        with open("score.json", "r") as file:
            content = json.load(file)
            return content
    except:
        return None