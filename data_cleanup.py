import os

def clean_temporary_data():
    rfid_data_path = 'assets/rfid_data/'
    backup_data_path = 'assets/backups/'

    for file_name in os.listdir(rfid_data_path):
        if file_name.endswith('.tmp'):
            os.remove(os.path.join(rfid_data_path, file_name))
            print(f"Temporary file {file_name} removed.")

    for file_name in os.listdir(backup_data_path):
        if file_name.endswith('.tmp'):
            os.remove(os.path.join(backup_data_path, file_name))
            print(f"Temporary file {file_name} removed.")
