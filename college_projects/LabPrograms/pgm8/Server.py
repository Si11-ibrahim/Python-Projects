import socket

host = '127.0.0.1'
port = 2045

msg = "This is a message..."
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
s.listen(1)
c, add = s.accept()

c.send(msg.encode("utf-8"))
s.close()

