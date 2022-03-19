import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('', 56789))

BUFFER_SIZE = 4096

with open('image2.jpeg', 'rb') as file:
	file_data = file.read(BUFFER_SIZE)

	While file_data:
		client.send(file_data)
		file_data = file.read(BUFFER_SIZE)

client.send(b"%IMAGE_COMPLETED%")



with open('image1.jpeg', 'wb') as file:
	recv_data = client.recv(BUFFER_SIZE)

 while recv_data:
                file.write(recv_data)
                recv_data = client_socket.recv(BUFFER_SIZE)

		 if recv_data == b"%IMAGE_COMPLETED%":
                break
