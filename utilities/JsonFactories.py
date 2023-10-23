import json


def readJson(directory, key: str):
    with open(directory, "r") as json_file:
        data = json.load(json_file)
    return data[key]


def writeJson(directory, key: str, new_value: str):
    with open(directory, "r") as json_file:
        data = json.load(json_file)
    data[key] = new_value
    with open(directory, 'w') as json_file:
        json.dump(data, json_file, indent=4)
