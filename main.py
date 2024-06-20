import ui
import auth

def main():
    if not auth.authenticate_user():
        print("Authentication failed. Exiting...")
        return

    ui.display_menu()

if __name__ == "__main__":
    main()
