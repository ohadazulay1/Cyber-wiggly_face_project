
from client import Client

class ClientHelperForOnline:
    _instance = None
    def __init__(self):
        if ClientHelperForOnline._instance is not None:
            raise Exception("This class is a singleton. Use get_instance() to obtain an instance.")

        ClientHelperForOnline._instance = self
        self.client = Client.get_instance()
        self.socket = self.client.get_connection()
        self.CODE_ONLINE_GAME = "5"

    @staticmethod
    def get_instance():
        if ClientHelperForOnline._instance is None:
            ClientHelperForOnline()
        return ClientHelperForOnline._instance



    def connectToAnotherUser(self, username) -> str:
        message = self.CODE_ONLINE_GAME + username
        self.socket.send((str.encode(message)))
        res = self.socket.recv(1024)
        data = res.decode('utf-8')
        return data
