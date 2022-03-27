from model.user import User
from utils.db import DbUtil

class UserManager:
    def createUser(user: User):
        query = "INSERT INTO users VALUES(" + user.getId() + " , '" + user.name + "' , '" + user.email + "' , '" + user.password + "')"
        DbUtil().insert(query)
