from utils.db import DbUtil

class Model:
    def print(self):
        print(vars(self))

        for key in vars(self):
            print(key + " : " + vars(self)[key])
    
    def getId(self):
        query = "SELECT id FROM " + vars(self)["table"] + " ORDER BY id DESC LIMIT 1"
        res = DbUtil().select(query)

        return str(res[0][0] + 1)
