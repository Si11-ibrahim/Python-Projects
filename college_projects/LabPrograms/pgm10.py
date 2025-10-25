import sys
import socket

buffer = b"1001010010100101001010101001"

while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("127.0.0.1", 2130))
        payload = b"101010101000010101010010101010" + buffer
        sock.send(payload)
        sock.close()
    except:
        print("Fuzzing crash at %s bytes" % str(len(buffer)))
        print("The extra bytes: ", buffer)
        sys.exit()
