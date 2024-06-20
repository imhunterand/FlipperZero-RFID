import json
import os

def export_card_data(card_id):
    file_path = f"assets/rfid_data/card_{card_id}.rfid"
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            card_data = json.load(file)
        export_file_path = f"assets/rfid_data/exported_card_{card_id}.json"
        with open(export_file_path, 'w') as export_file:
            json.dump(card_data, export_file)
        print(f"Card data exported to {export_file_path}")
    else:
        print(f"No card found with ID {card_id}")

def import_card_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            card_data = json.load(file)
        save_path = f"assets/rfid_data/card_{card_data['id']}.rfid"
        with open(save_path, 'w') as save_file:
            json.dump(card_data, save_file)
        print(f"Card data imported from {file_path}")
    else:
        print(f"No file found at {file_path}")
