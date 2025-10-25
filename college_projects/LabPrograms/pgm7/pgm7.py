import socket

ip = socket.gethostbyname(socket.gethostname())
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for port in range(65535):
    try:
        serv.bind((ip, port))
    except:
        print('[OPEN] port open: ', port)
        serv.close()
