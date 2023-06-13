from client import Client


class ClientHelperForOnlineEndGame:
    gameOn = True
    _instance = None

    def __init__(self):
        self.CODE_ONLINE_GAME_ENDED = "6"
        if ClientHelperForOnlineEndGame._instance is not None:
            raise Exception("This class is a singleton. Use get_instance() to obtain an instance.")

        ClientHelperForOnlineEndGame._instance = self
        self.client = Client.get_instance()
        self.socket = self.client.get_connection()

    @staticmethod
    def get_instance():
        if ClientHelperForOnlineEndGame._instance is None:
            ClientHelperForOnlineEndGame()
        return ClientHelperForOnlineEndGame._instance


    def IHaveLost(self, oppUserName):
        self.gameOver()
        print("i lost")
        message = self.CODE_ONLINE_GAME_ENDED + oppUserName
        self.socket.send((str.encode(message)))

    def didIWin(self):
        res = self.socket.recv(1024)
        if self.gameOn:
            print("i won")
            self.gameOver()

        #data = res.decode('utf-8')
       # return True

    def getGameOn(self):
        return self.gameOn

    def gameOver(self):
        self.gameOn = False

    def newGame(self):
        self.gameOn = True

