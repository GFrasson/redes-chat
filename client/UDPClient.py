import socket
import json


class UDPClient:
    def __init__(self):
        self.server_address = "127.0.0.1"
        self.server_port = 20001
        self.buffer_size = 1024
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.headers = {
            'path': '/'
        }
        self.body = {}

    def get(self, body: dict, headers: dict[str, str] = {}):
        self.prepare_request_content(body, headers)        
        self.send_request()

        response = self.get_response()
        return response

    def prepare_request_content(self, body: dict, headers: dict[str, str] = {}):
        for key, value in body.items():
            self.body[key] = value
        
        for key, value in headers.items():
            self.headers[key] = value

    def send_request(self) -> None:
        request_content = self.request_content_string
        request_bytes_to_send = str.encode(request_content)

        self.socket.sendto(request_bytes_to_send, (self.server_address, self.server_port))
    
    def get_response(self):
        response_encoded, address = self.socket.recvfrom(self.buffer_size)
        response_decoded = response_encoded.decode()
        response = json.loads(response_decoded)
        
        return response
    
    @property
    def request_content_string(self) -> str:
        return json.dumps(self.request_content)
    
    @property
    def request_content(self) -> dict:
        return {
            'headers': self.headers,
            'body': self.body
        }
