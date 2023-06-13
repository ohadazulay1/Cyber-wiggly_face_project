import socket
import ssl
from _thread import *
import pickle
from sereverHelper import ServerHelper
from onlineUsers import OnlineUsers

ServerSideSocket = socket.socket()
HOST = '127.0.0.1'
PORT = 2130
ThreadCount = 0
LOGIN_NUM = 0
SIGN_UP_NUM = 1
GET_TOP_NUM = 2
GET_SELF_HIGHSCORE_NUM = 3
SET_NEW_HGIHSCORE_NUM = 4
PLAY_ONLINE = 5
ONLINE_PLAYER_HIT = 6
STARTING_SCORE = "0"

CODE_SUCCESS = "0"
CODE_FAILED = "1"

mapUsersConn = {}

serverCertFile = "./server.crt"
serverPrivateKey = "./server.key"
dataBaseHelper = ServerHelper()

try:
    ServerSideSocket.bind((HOST, PORT))
except socket.error as e:
    raise Exception(str(e))

print('Socket is listening..')
ServerSideSocket.listen(5)

def multi_threaded_client(ssl_socket):
    ssl_socket.send(str.encode('Server is working:'))
    isDict = False
    response = ''
    while True:
        data = ssl_socket.recv(1024)
        decoded_data = data.decode()

        guideNum = decoded_data[0]
        newData = decoded_data[1:]

        if guideNum == str(LOGIN_NUM):
            if dataBaseHelper.login(newData):
                response = CODE_SUCCESS + 'there is a user with this username and password'
                splited_data = newData.split(",")
                username = splited_data[0]
                mapUsersConn[username] = ssl_socket
            else:
                response = CODE_FAILED + 'there is no user with this username and password'
            ssl_socket.sendall(str.encode(response))


        elif guideNum == str(SIGN_UP_NUM):
            if dataBaseHelper.signUp(newData, STARTING_SCORE):
                response = CODE_SUCCESS + 'You are now in the DB'
                splited_data = newData.split(",")
                username = splited_data[0]
                mapUsersConn[username] = ssl_socket
            else:
                response = CODE_FAILED + 'A user with the same username is already exist in the system'
            ssl_socket.sendall(str.encode(response))


        elif guideNum == str(GET_TOP_NUM):
            response = dataBaseHelper.topFive()
            dictToSend = pickle.dumps(response)
            ssl_socket.sendall(dictToSend)
           # isDict = True


        elif guideNum == str(GET_SELF_HIGHSCORE_NUM):
            response = dataBaseHelper.getSelfHighScore(newData)
            ssl_socket.sendall(str.encode(response))



        elif guideNum == str(SET_NEW_HGIHSCORE_NUM):
            response = dataBaseHelper.setSelfHighScore(newData)
            ssl_socket.sendall(str.encode(response))


        elif guideNum == str(PLAY_ONLINE):
            username = newData
            found, otherUsername = OnlineUsers.getOnlineUserToPlay(username)
            if found:
                response = otherUsername
                otherSocket = mapUsersConn.get(otherUsername)
                otherSocket.sendall(str.encode(username))
                ssl_socket.sendall(str.encode(otherUsername))

            else:
                OnlineUsers.addPendingUser(username)


        elif guideNum == str(ONLINE_PLAYER_HIT):
            oppUsername = newData
            otherSocket = mapUsersConn.get(oppUsername)
            otherSocket.sendall(str.encode(CODE_SUCCESS))
            ssl_socket.sendall(str.encode(CODE_SUCCESS))


        if not data:
            break

    ssl_socket.close()


while True:
    client_socket, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))

    # Wrap the socket with SSL/TLS
    ssl_socket = ssl.wrap_socket(client_socket, server_side=True, certfile=serverCertFile, keyfile=serverPrivateKey)

    start_new_thread(multi_threaded_client, (ssl_socket, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()