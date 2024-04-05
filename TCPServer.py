from socket import *

serverSocket=socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('',12332))
serverSocket.listen(5)
print("server is ready to receive")
while True:
    connectionSocket,addr=serverSocket.accept()
    sentence=connectionSocket.recv(1024).decode()
    captalizedSentence=sentence.upper()
    connectionSocket.send(captalizedSentence.encode())
    connectionSocket.close()    