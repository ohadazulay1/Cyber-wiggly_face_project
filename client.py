import socket
import pickle
import ssl

class Client:
    _instance = None

    #HOST = '127.0.0.1'
    HOST = '192.168.7.13'
    #HOST = '172.20.10.2'
    PORT = 2132
    SERVER_CA_CERT_FILE = "./server.crt"
    CODE_LOGIN = "0"
    CODE_SIGN_UP = "1"
    CODE_HIGH_SCORES = "2"
    CODE_GET_SELF_HIGH_SCORE = "3"
    CODE_SET_SELF_HIGH_SCORE = "4"
    CODE_ONLINE_GAME = "5"

    CODE_RECEIVE_SUCCESS = "0"
    CODE_RECEIVE_FAILED = "1"

    def __init__(self):
        if Client._instance is not None:
            raise Exception("This class is a singleton. Use get_instance() to obtain an instance.")

        Client._instance = self
        clientMultiSocket = socket.socket()

        # Wrap the socket with SSL/TLS
        self.ssl_socket = ssl.wrap_socket(clientMultiSocket, cert_reqs=ssl.CERT_REQUIRED, ca_certs=self.SERVER_CA_CERT_FILE)

        try:
            self.ssl_socket.connect((self.HOST, self.PORT))
        except socket.error as e:
            raise Exception(str(e))

        res = self.ssl_socket.recv(1024)

    @staticmethod
    def get_instance():
        if Client._instance is None:
            Client()
        return Client._instance


    def get_connection(self):
        return self.ssl_socket


    def login(self, username, password) -> bool:
        message = self.CODE_LOGIN + username + "," + password
        self.ssl_socket.send(str.encode(message))
        res = self.ssl_socket.recv(1024)
        data = res.decode('utf-8')
        guideNum = data[0]
        newData = data[1:]

        if guideNum == self.CODE_RECEIVE_SUCCESS:
            return True
        elif guideNum == self.CODE_RECEIVE_FAILED:
            return False


    def signUp(self, username, password) -> bool:
        message = self.CODE_SIGN_UP + username + "," + password
        self.ssl_socket.send(str.encode(message))
        res = self.ssl_socket.recv(1024)
        data = res.decode('utf-8')
        guideNum = data[0]
        newData = data[1:]
        if guideNum == self.CODE_RECEIVE_SUCCESS:
            return True
        elif guideNum == self.CODE_RECEIVE_FAILED:
            return False


    def topFive(self) -> dict:
        message = self.CODE_HIGH_SCORES
        self.ssl_socket.send(str.encode(message))
        receivedData = b''
        res = self.ssl_socket.recv(4096)
        receivedData += res
        received_dict = pickle.loads(receivedData)
        return received_dict


    def getSelfHighScore(self, username: str) -> float:
        message = self.CODE_GET_SELF_HIGH_SCORE + username
        self.ssl_socket.send(str.encode(message))
        res = self.ssl_socket.recv(1024)
        data = res.decode('utf-8')
        return float(data)


    def setSelfHighScore(self, username, newHighScore):
        message = self.CODE_SET_SELF_HIGH_SCORE + username + "," + str(newHighScore)
        self.ssl_socket.send(str.encode(message))
        res = self.ssl_socket.recv(1024)
        data = res.decode('utf-8')


  #  def connectToAnotherUser(self, username):
   #     message = self.CODE_ONLINE_GAME + username
    #    self.ssl_socket.send((str.encode(message)))
     #   res = self.ssl_socket.recv(1024)
      #  data = res.decode('utf-8')
       # return data