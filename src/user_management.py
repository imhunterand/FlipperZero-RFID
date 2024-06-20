users = []

def add_user(username, password):
    users.append({'username': username, 'password': password})
    print(f"User {username} added.")

def remove_user(username):
    global users
    users = [user for user in users if user['username'] != username]
    print(f"User {username} removed.")

def list_users():
    if not users:
        print("No users found.")
    else:
        print("Registered users:")
        for user in users:
            print(f"Username: {user['username']}")
