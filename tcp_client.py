import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',9999))

client.send("Hello Server".encode('utf_8'))
print(client.recv(1024).decode('utf-8'))
client.send("Bye see ya".encode('utf_8'))
print(client.recv(1024).decode('utf-8'))