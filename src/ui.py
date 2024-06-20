import rfid_reader
import rfid_writer
import encryption
import logger
import utils
import stats
import user_management
import config_manager
import card_search
import data_cleanup
import data_export_import
import email_notifications

def display_menu():
    while True:
        print("\nMenu:")
        print("1. Read RFID Card")
        print("2. Write RFID Card")
        print("3. Encrypt Card Data")
        print("4. Decrypt Card Data")
        print("5. Backup Card Data")
        print("6. Restore Card Data")
        print("7. View Stats")
        print("8. User Management")
        print("9. Config Management")
        print("10. Search Card by ID")
        print("11. Clean Temporary Data")
        print("12. Export Card Data")
        print("13. Import Card Data")
        print("14. Send Email Notification")
        print("15. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            card_data = rfid_reader.read_card()
            utils.save_card_data(card_data)
            logger.log_activity("Read", card_data['id'])
        elif choice == '2':
            card_data = utils.load_card_data()
            if card_data:
                rfid_writer.write_card(card_data)
                logger.log_activity("Write", card_data['id'])
        elif choice == '3':
            card_data = utils.load_card_data()
            if card_data:
                encrypted_data = encryption.encrypt_data(card_data)
                utils.save_card_data(encrypted_data, encrypted=True)
                logger.log_activity("Encrypt", card_data['id'])
        elif choice == '4':
            card_data = utils.load_card_data(encrypted=True)
            if card_data:
                decrypted_data = encryption.decrypt_data(card_data)
                utils.save_card_data(decrypted_data)
                logger.log_activity("Decrypt", card_data['id'])
        elif choice == '5':
            card_data = utils.load_card_data()
            if card_data:
                utils.backup_card_data(card_data)
                logger.log_activity("Backup", card_data['id'])
        elif choice == '6':
            utils.restore_card_data()
            logger.log_activity("Restore", "N/A")
        elif choice == '7':
            stats.display_stats()
        elif choice == '8':
            user_management_menu()
        elif choice == '9':
            config_manager_menu()
        elif choice == '10':
            card_id = input("Enter card ID to search: ")
            card_search.search_card_by_id(card_id)
        elif choice == '11':
            data_cleanup.clean_temporary_data()
        elif choice == '12':
            card_id = input("Enter card ID to export: ")
            data_export_import.export_card_data(card_id)
        elif choice == '13':
            file_path = input("Enter the path of the file to import: ")
            data_export_import.import_card_data(file_path)
        elif choice == '14':
            subject = input("Enter email subject: ")
            message = input("Enter email message: ")
            recipient = input("Enter recipient email: ")
            email_notifications.send_email_notification(subject, message, recipient)
        elif choice == '15':
            break
        else:
            print("Invalid choice. Please try again.")

def user_management_menu():
    while True:
        print("\nUser Management Menu:")
        print("1. Add User")
        print("2. Remove User")
        print("3. List Users")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_management.add_user(username, password)
        elif choice == '2':
            username = input("Enter username to remove: ")
            user_management.remove_user(username)
        elif choice == '3':
            user_management.list_users()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def config_manager_menu():
    config = config_manager.load_config()
    while True:
        print("\nConfig Management Menu:")
        print("1. View Config")
        print("2. Edit Config")
        print("3. Save Config")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")
        if choice == '1':
            print("Current Configuration:")
            print(config)
        elif choice == '2':
            key = input("Enter config key to edit: ")
            value = input("Enter new value: ")
            config[key] = value
        elif choice == '3':
            config_manager.save_config(config)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
