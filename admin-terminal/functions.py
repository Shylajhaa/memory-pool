from model.user import User
from core.users import UserManager as user_manager

class Functions:
    def invoke(self, method_name):
        getattr(self, method_name)()

    def signup(self):
        user_name = input("Enter User Name")
        email = input("Enter email")
        password = input("Enter password")

        user = User(user_name, email, password)
        user_manager.createUser(user)
