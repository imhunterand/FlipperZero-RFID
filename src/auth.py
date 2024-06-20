import getpass

registered_users = [
    {'username': 'admin', 'password': 'admin'}
]

def authenticate_user():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    for user in registered_users:
        if user['username'] == username and user['password'] == password:
            print("Authentication successful.")
            return True

    print("Authentication failed.")
    return False
