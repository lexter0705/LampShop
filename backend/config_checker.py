import json


def get_data():
    with open("./config_checker.py", encoding="utf-8", mode="r") as read_file:
        data = json.load(read_file)

    return data