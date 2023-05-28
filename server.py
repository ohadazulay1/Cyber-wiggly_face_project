import socket
import ssl
from _thread import *
import pickle
from sereverHelper import ServerHelper

ServerSideSocket = socket.socket()
HOST = '127.0.0.1'
PORT = 2123
ThreadCount = 0
LOGIN_NUM = 0
SIGN_UP_NUM = 1
GET_TOP_NUM = 2
GET_SELF_HIGHSCORE_NUM = 3
SET_NEW_HGIHSCORE_NUM = 4
STARTING_SCORE = "0"

CODE_SUCCESS = "0"
CODE_FAILED = "1"

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
                print('there is a user with this username and password')
            else:
                response = CODE_FAILED + 'there is no user with this username and password'
                print('there is not a user with this username and password')

        elif guideNum == str(SIGN_UP_NUM):
            if dataBaseHelper.signUp(newData, STARTING_SCORE):
                response = CODE_SUCCESS + 'You are now in the DB'
            else:
                response = CODE_FAILED + 'A user with the same username is already exist in the system'


        elif guideNum == str(GET_TOP_NUM):
            response = dataBaseHelper.topFive()
            isDict = True


        elif guideNum == str(GET_SELF_HIGHSCORE_NUM):
            response = dataBaseHelper.getSelfHighScore(newData)


        elif guideNum == str(SET_NEW_HGIHSCORE_NUM):
            response = dataBaseHelper.setSelfHighScore(newData)


        if isDict == True:
            isDict = False
            dictToSend = pickle.dumps(response)
            ssl_socket.sendall(dictToSend)
        else:
            ssl_socket.sendall(str.encode(response))

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