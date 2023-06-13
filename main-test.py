from client import Client
from clientHelperForOnline import ClientHelperForOnline
from PyQt5.QtWidgets import QApplication

import sys

class Main:

    if __name__ == '__main__':
        app = QApplication(sys.argv)

        client = Client.get_instance()
        client.login("ohad", "1")

        message = "5" + "ohad"
        print("1")
        socket = client.get_connection()
        print("2")
        socket.send((str.encode(message)))
        print("3")
        res = socket.recv(1024)
        print("4")
        data = res.decode('utf-8')

     #   ch = ClientHelperForOnline.get_instance()
     #   ch.connectToAnotherUser("ohad")




        sys.exit(app.exec_())
