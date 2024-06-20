import json

config_file_path = 'config/config.json'

def load_config():
    with open(config_file_path, 'r') as file:
        config = json.load(file)
    print("Configuration loaded.")
    return config

def save_config(config):
    with open(config_file_path, 'w') as file:
        json.dump(config, file)
    print("Configuration saved.")
