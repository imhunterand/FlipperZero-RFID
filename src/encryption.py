import json
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_data(card_data):
    card_data_json = json.dumps(card_data)
    encrypted_data = cipher.encrypt(card_data_json.encode())
    encrypted_card_data = {
        'id': card_data['id'],
        'data': encrypted_data.decode()
    }
    print(f"Data encrypted for card ID = {card_data['id']}")
    return encrypted_card_data

def decrypt_data(encrypted_card_data):
    encrypted_data = encrypted_card_data['data'].encode()
    decrypted_data_json = cipher.decrypt(encrypted_data).decode()
    decrypted_data = json.loads(decrypted_data_json)
    print(f"Data decrypted for card ID = {encrypted_card_data['id']}")
    return decrypted_data
