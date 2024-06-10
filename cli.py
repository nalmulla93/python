class CommandLineInterface:
    def __init__(self, app):
        self.app = app

    def start(self):
        while True:
            command = input("Enter a command (login, logout, create_item, get_items, get_user_items, remove_user, get_users, exit): ")
            print(f"Received command: {command}")  # Debug print statement
            if command == "login":
                username = input("Enter username: ")
                role = input("Enter role (admin or user): ")
                self.app.login(username, role)
                print(f"Logged in as {username} with role {role}")  # Debug print statement
            elif command == "logout":
                self.app.logout()
                print("Logged out")  # Debug print statement
            elif command == "create_item":
                item_type = input("Enter item type (lyric, music_score, audio_recording): ")
                content = input("Enter item content: ")
                self.app.create_item(item_type, content)
                print(f"Created item of type {item_type} with content: {content}")  # Debug print statement
            elif command == "get_items":
                items = self.app.get_items()
                for item in items:
                    print(item.decrypt())
                print("Displayed all items")  # Debug print statement
            elif command == "get_user_items":
                user_items = self.app.get_user_items()
                for item in user_items:
                    print(item.decrypt())
                print("Displayed user items")  # Debug print statement
            elif command == "remove_user":
                username = input("Enter username to remove: ")
                self.app.remove_user(username)
                print(f"Removed user {username}")  # Debug print statement
            elif command == "get_users":
                users = self.app.get_users()
                for user in users:
                    print(user.username)
                print("Displayed all users")  # Debug print statement
            elif command == "exit":
                print("Exiting application")  # Debug print statement
                break
            else:
                print("Invalid command")  # Debug print statement
