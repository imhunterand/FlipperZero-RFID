import os
import json
import shutil

def save_card_data(card_data, encrypted=False):
    file_path = f"assets/rfid_data/card_{card_data['id']}.rfid"
    if encrypted:
        file_path = f"{file_path}.enc"
    with open(file_path, 'w') as file:
        json.dump(card_data, file)
    print(f"Card data saved to {file_path}")

def load_card_data(encrypted=False):
    card_id = input("Enter card ID to load: ")
    file_path = f"assets/rfid_data/card_{card_id}.rfid"
    if encrypted:
        file_path = f"{file_path}.enc"
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            card_data = json.load(file)
        print(f"Card data loaded from {file_path}")
        return card_data
    else:
        print(f"No data found for card ID {card_id}")
        return None

def backup_card_data(card_data):
    file_path = f"assets/rfid_data/card_{card_data['id']}.rfid"
    backup_path = f"assets/backups/card_{card_data['id']}.rfid.bak"
    shutil.copy(file_path, backup_path)
    print(f"Card data backed up to {backup_path}")

def restore_card_data():
    backup_files = os.listdir("assets/backups/")
    if not backup_files:
        print("No backup files found.")
        return
    print("Available backups:")
    for i, file in enumerate(backup_files):
        print(f"{i+1}. {file}")
    choice = int(input("Enter the number of the backup file to restore: ")) - 1
    if 0 <= choice < len(backup_files):
        backup_file = backup_files[choice]
        original_file = backup_file.replace(".bak", "")
        shutil.copy(f"assets/backups/{backup_file}", f"assets/rfid_data/{original_file}")
        print(f"Backup {backup_file} restored to {original_file}")
    else:
        print("Invalid choice.")
