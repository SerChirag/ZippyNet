import socket

ssFT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssFT.bind(('', 8756))
ssFT.listen(1)
print("Server running...")
fileNo = 0
while True:
    (conn, address) = ssFT.accept()
    file = str(fileNo)
    fileNo += 1

    #Receive, output and save file
    with open(file, "wb") as fw:
        print("Receiving "+file)
        while True:
            print('receiving file '+file)
            data = conn.recv(10485760)
            print('Received '+file)
            if not data:
                print('Breaking from file write')
                break
            fw.write(data)
        print('Wrote to file')
        fw.close()
        print("Received..")

        (conn, address) = ssFT.accept()
        conn.sendall(file)
        print("url sent")
ssFT.close()