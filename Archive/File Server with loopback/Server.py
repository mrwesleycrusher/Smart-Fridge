import socket
import threading
import os

def RetrFile(name, sock):
    filename = sock.recv(1024)
    if os.path.isfile(filename.decode()):
        sock.send(("EXISTS " + str(os.path.getsize(filename.decode()))).encode())
        userResponse = sock.recv(1024)
        if userResponse[:2] == 'OK'.encode():
            with open(filename.decode(), 'rb') as f:
                bytesToSend = f.read(1024)
                sock.send(bytesToSend)
                while bytesToSend != "":
                    bytesToSend = f.read(1024)
                    sock.send(bytesToSend)
    else:
        sock.send("ERR ".encode())

    sock.close()

def Main():
    # we need to define a host and port to connect to so we can do a file transfer
    host = '127.0.0.1'
    port = 5000


    s = socket.socket()
    s.bind((host,port))

    s.listen(5)

    print("Server Started.")

    while True:
        c, addr = s.accept()
        print("client connedted ip:<" + str(addr) + ">")
        t = threading.Thread(target=RetrFile, args=("RetrThread", c))
        t.start()
         
    s.close()

if __name__ == '__main__':
    Main()
