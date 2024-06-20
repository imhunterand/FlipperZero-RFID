import logging

logging.basicConfig(filename='logs/activity.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_activity(action, card_id):
    logging.info(f"Action: {action}, Card ID: {card_id}")
    print(f"Logged: {action} for Card ID {card_id}")
