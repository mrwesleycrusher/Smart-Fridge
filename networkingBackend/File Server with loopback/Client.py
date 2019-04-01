import socket

def Main():
    #we again need to assign an IP and port for our program
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    filename = input("Filename? -> ")
    if filename != 'q':
        s.send(filename.encode())
        data = s.recv(1024)
        if data[:6] == 'EXISTS'.encode():
            filesize = int(data[6:])
            message = input("File exists, " + str(filesize) +"Bytes, download? (Y/N)? -> ")
            if message == 'Y':
                s.send("OK".encode())
                f = open(filename+'.new', 'wb')
                data = s.recv(1024)
                totalRecv = len(data)
                f.write(data)
                while totalRecv < filesize:
                    data += s.recv(1024)
                    totalRecv += len(data)
                    print("{0:.2f}".format((totalRecv/float(filesize))*100)+ "% Done")
                print("Download Complete!")
                f.write(data)
                f.close()
        else:
            print("File Does Not Exist!")

    s.close()
    

if __name__ == '__main__':
    Main()
