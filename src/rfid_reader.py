import random

def read_card():
    # Simulasi membaca data kartu RFID
    card_id = random.randint(1000, 9999)
    card_data = {
        'id': card_id,
        'data': f"Sample data for card {card_id}"
    }
    print(f"Card Read: ID = {card_id}")
    return card_data
