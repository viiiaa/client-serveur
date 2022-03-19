import io
import socket

from PIL import Image
from PIL import ImageFilter

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('',56789))

server.listen()

BUFFER_SIZE = 4096

while True:
	client_socket, _ = server.accept()
 if recv_data == b"%IMAGE_COMPLETED%":
                break

	with open('image1.jpeg','wb') as file:
	recv_data = client_socket.recv(BUFFER_SIZE)
	while recv_data:
		file.write(recv_data)
		recv_data = client_socket.recv(BUFFER_SIZE)

image = Image.open(file_stream)


	if recv_data == b"%IMAGE_COMPLETED%":
		break


image.tobytes()
image = Image.open(file_stream)
image.save('image2.jpeg', format='JPEG')

with open('image1.jpeg','wb') as file:
        recv_data = client_socket.recv(BUFFER_SIZE)

	while file_data:
		client_socket.send(file_data)
		file_data = file.read(BUFFER_SIZE)
 if recv_data == b"%IMAGE_COMPLETED%":
                break

		client_socket.send(b"%IMAGE_COMPLETED%")

		os.unlink('image1.jpeg')
