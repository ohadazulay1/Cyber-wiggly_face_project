from builtins import tuple

class OnlineUsers:

    usersPendingOnline = []

    #מחזיר נכון ואת שם המשתמש שמחכה -- או לא נכון ומחרוזת ריקה אם אין. מוציאה את המשתמש מהממתינים אם קיים
    @staticmethod
    def getOnlineUserToPlay(myUserName) -> tuple[bool, str]:
        if OnlineUsers.usersPendingOnline and (myUserName not in OnlineUsers.usersPendingOnline or len(OnlineUsers.usersPendingOnline) > 1):
            username = OnlineUsers.usersPendingOnline.pop()
            return True, username
        else:
            return False, ""

    #מוסיף לממתינים
    @staticmethod
    def addPendingUser(username: str):
        OnlineUsers.usersPendingOnline.append(username)
