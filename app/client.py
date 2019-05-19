import socket
# Returns a string which is name of file in server directory
def sendToServer(filename):
    csFT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    csFT.connect(('10.8.17.11', 8756))
    with open(filename, 'rb') as fs: 
        while True:
            data = fs.read()
            print('Sending file '+file)
            csFT.sendall(data)
            print('Sent file '+file)
            if not data:
                print('Breaking from sending data')
                break
        fs.close()
    csFT.close()

    # Recieving URL
    csFT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    csFT.connect(('10.8.17.11', 8756))
    url = csFT.recv(1024)
    print("file is hosted at : "+url)
    csFT.close()

    return url


print(sendToServer('autoencoder.h5'))