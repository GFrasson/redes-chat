import socket
import json
from providers.BaseClient import BaseClient


class TCPClient(BaseClient):
    def __init__(self):
        super().__init__(server_addess="127.0.0.1", server_port=32007, buffer_size=1024)

        self.socket = socket.socket()
        self.socket.connect((self.server_address, self.server_port))

    def send_request(self) -> None:
        self.socket.send(self.request_bytes_to_send)
    
    def get_response(self):
        response_encoded = self.socket.recv(self.buffer_size)
        response_decoded = response_encoded.decode()
        response = json.loads(response_decoded)
        
        return response
