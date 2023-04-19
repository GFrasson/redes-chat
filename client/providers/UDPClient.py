import socket
import json

from providers.BaseClient import BaseClient


class UDPClient(BaseClient):
    def __init__(self):
        super().__init__(server_addess="127.0.0.1", server_port=20001, buffer_size=1024)

        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    def send_request(self) -> None:
        self.socket.sendto(self.request_bytes_to_send, (self.server_address, self.server_port))
    
    def get_response(self):
        response_encoded, address = self.socket.recvfrom(self.buffer_size)
        response_decoded = response_encoded.decode()
        response = json.loads(response_decoded)
        
        return response
