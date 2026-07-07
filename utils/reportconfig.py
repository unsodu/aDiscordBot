import json
import os

FILE = "reportchannel.json"

def save_channel(channel_id):
    with open(FILE, "w") as f:
        json.dump({"channel_id": channel_id}, f)

def get_channel():
    if not os.path.exists(FILE):
        return None

    with open(FILE, "r") as f:
        data = json.load(f)

    return data.get("channel_id")