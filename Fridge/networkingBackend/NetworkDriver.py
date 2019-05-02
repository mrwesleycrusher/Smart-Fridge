#this class runs on the host computer to connect it to the
#raspi zero to abstract the biolerplate of connecting, sending
#commands, and receiving images from the pi camera
import socket
import subprocess
import re, threading


class NetworkDriver:
    def __init__(self, type):
        if type == 'laptop':
            self.lock = threading.Lock()
            self.port = 5000
            #find raspberry pi ip address
            p1 = subprocess.Popen(['cat', '/var/lib/misc/dnsmasq.leases'], stdout=subprocess.PIPE)
            #assign host to the ip address contained in the output of the subprocess
            self.host = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",p1.communicate()[0].decode())[0]
            self.sock = socket.socket()
            self.sock.connect((self.host, self.port))
        if type == 'pi':
            self.lock = threading.Lock()
            self.host = socket.gethostname() 
            self.port = 5000
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.bind(('',self.port))
            #look for backlog
            self.sock.listen(5)
            #accept incoming connection, since we don't support multiple 
            #clients at once, just assign sock to the connection
            self.sock, self.clientIP = self.sock.accept()
            self.most_recent_command = None
            self.killthread = False


    #takes an unencoded string and sends it to the server
    def send(self, information):
        with self.lock:
            #we need to tell the other end how much we are sending
            self.sock.sendall(str(len(information.encode())).encode())
            #check for 'ack'
            ack = None 
            while ack != 'ack':
                ack = self.sock.recv(1024).decode()
            #now we need to actually send the data over the socket
            self.sock.sendall(information.encode())
            ack = None
            #now of course we wait for ack again
            while ack != 'ack':
                ack = self.sock.recv(1024).decode()
        #@Tyler changed =>>> (line 43 and 49) socket.recieve(3) -> self.sock.recv(1024)

    #receives an unencoded string from the server
    def receive(self):
        with self.lock:
            transferSize = self.sock.recv(1024).decode()
            self.sock.sendall('ack'.encode())
            transfer = self.sock.recv(transferSize).decode()
            self.sock.sendall('ack'.encode())
            return transfer
    #@Tyler changed socket.sendall -> self.sock.sendall
    
    def __del__(self):
        with self.lock:
            self.sock.close()
