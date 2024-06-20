import os
import json

def search_card_by_id(card_id):
    file_path = f"assets/rfid_data/card_{card_id}.rfid"
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            card_data = json.load(file)
        print(f"Card found: {card_data}")
        return card_data
    else:
        print(f"No card found with ID {card_id}")
        return None
