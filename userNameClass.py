
class UserNameClass:
    _instance = None

    def __init__(self):
        if UserNameClass._instance is not None:
            raise Exception("This class is a singleton. Use get_instance() to obtain an instance.")

        UserNameClass._instance = self

    @staticmethod
    def get_instance():
        if UserNameClass._instance is None:
            UserNameClass()
        return UserNameClass._instance

    def setUserName(self, newUserName):
        self.username = newUserName

    def getUserName(self):
        return self.username
