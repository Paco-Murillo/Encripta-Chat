import threading#Los hilos...
import socket#The socket library
import sys

mess = True
print(f"Running the server on: {socket.gethostname()} and port: {1024}")

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind((socket.gethostname(), 1024))
serverSocket.listen(1)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def new_client(client, connection, clientName):#Wherever a client is connected...
	global mess
	ip = connection[0]
	port = connection[1]
	# print(f"The new connection was made from IP: {ip}, and port: {port}!")
	while True:
		msg = client.recv(1024)
		if msg.decode() == 'exit' or msg.decode() == "":
			break
		print(f"\n{clientName} said: {msg.decode()}\nMessage: ", end="")   # Esta linea se modificara cuando se implemente la encriptación
	print(f"{clientName} left!")
	serverSocket.close()
	clientSocket.close()
	client.close()
	mess = False
	sys.stdin = "\n"


def new_message():
	global mess
	while mess:
		msg = input("Message: ")  # The message sent...
		if mess:
			clientSocket.sendall(msg.encode('utf-8'))
		if msg == 'exit':
			# print("Client left!!")
			threading.main_thread()
			raise Exception("Client disconnect.")
		'''
		data = s.recv(1024)  # Length in bytes of the message received.
		print(f"The server response was: {data.decode()}")
		'''
	serverSocket.close()
	clientSocket.close()
	mess = False


#Infinite loop... waiting for any request of clients...
def main():
	try:
		client, adr = serverSocket.accept()  # Once a client is connected
		clientSocket.connect((socket.gethostname(), 1025))
		clientName = input("What's your name: ")
		clientSocket.sendall(clientName.encode('UTF-8'))
		clientName = client.recv(1025).decode()
		serverThread = threading.Thread(target=new_client, args=(client, adr, clientName))
		serverThread.start()
		new_message()
	except Exception as e:
		print(f"{e}")

main()

serverSocket.close()
clientSocket.close()
print(threading.activeCount())


