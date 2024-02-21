import ssl
import socket

def secure_communication_server():
   context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
   context.load_cert_chain(certfile="server_certificate.pem", keyfile="server_private_key.pem")

   server_socket = context.wrap_socket(socket.socket(), server_side=True)
   server_socket.bind(('localhost', 12345))
   server_socket.listen(5)

   while True:
       client_socket, address = server_socket.accept()
       data = client_socket.recv(1024)
       print(f"Received: {data.decode()}")
       client_socket.close()

secure_communication_server()