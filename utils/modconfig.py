import json
import os

FILE = "modconfig.json"

def load():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def set_modchannel(guild_id, channel_id):
    data = load()
    data[str(guild_id)] = channel_id
    save(data)

def get_modchannel(guild_id):
    data = load()
    return data.get(str(guild_id))