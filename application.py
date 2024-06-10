from database import Database
from user import User, Admin
from item import ItemFactory
from cli import CommandLineInterface

class Application:
    def __init__(self):
        self.database = Database()  # Singleton pattern for Database
        self.admin = Admin("admin")
        self.current_user = None
        self.cli = CommandLineInterface(self)

    def run(self):
        self.cli.start()

    def login(self, username, role):
        if role == "admin":
            self.current_user = self.admin
        else:
            user = next((u for u in self.admin.get_users() if u.username == username), None)
            if not user:
                user = User(username)
                self.admin.add_user(user)
            self.current_user = user

    def logout(self):
        self.current_user = None
    def create_item(self, item_type, content):
        item = ItemFactory.create_item(item_type, content)
        self.database.add_item(item)
        self.current_user.add_item(item)

    def get_items(self):
        return self.database.get_items()

    def get_user_items(self):
        return self.current_user.get_items()

    def remove_user(self, username):
        user = next((u for u in self.admin.get_users() if u.username == username), None)
        if user:
            self.admin.remove_user(user)

    def get_users(self):
        return self.admin.get_users()
