from utils.model import Model

class User(Model):
    def __init__(self, name, email, password) -> None:
        self.table = "users"
        self.name = name
        self.email = email
        self.password = password
