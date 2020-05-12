import socket


print(f"Connecting to server: {socket.gethostname()} on port: {1024}")
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1024))


while True:

    msg=input("What do we want to send to server??")#The message sent...
    s.sendall(msg.encode('utf-8'))

    if msg=='exit':
        print("Client left!!")
        break
    data=s.recv(1024)#Length in bytes of the message received.
    print(f"The server response was: {data.decode()}")


