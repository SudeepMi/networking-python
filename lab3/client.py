import ssl
import socket

def secure_communication_client():
   context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
   context.load_cert_chain(certfile="client_certificate.pem", keyfile="client_private_key.pem")

   # Disable certificate verification
   context.check_hostname = False
   context.verify_mode = ssl.CERT_NONE

   with context.wrap_socket(socket.socket(), server_hostname='localhost') as client_socket:
       client_socket.connect(('localhost', 12345))
       message = "Hello, secure server!"
       client_socket.send(message.encode())


secure_communication_client()