import socket

host = '127.0.0.1'
port = 2045
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))
c = s.recv(1024)
print(c.decode("utf-8"))
s.close()

