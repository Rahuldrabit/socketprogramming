from socket import *

clientSocket=socket(AF_INET,SOCK_STREAM)

clientSocket.connect(('192.168.0.103',12332))
sentence=input('Input lowercase sentence: ')
clientSocket.send(sentence.encode())
ackSentence=clientSocket.recv(1024)
print("From server: ",ackSentence.decode())
clientSocket.close()