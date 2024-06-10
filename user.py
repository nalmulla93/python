class User:
    def __init__(self, username):
        self.username = username
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_items(self):
        return self.items

class Admin(User):
    def __init__(self, username):
        super().__init__(username)
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def get_users(self):
        return self.users
