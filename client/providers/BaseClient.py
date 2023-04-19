import json
from abc import ABC, abstractmethod


class BaseClient(ABC):
    def __init__(self, server_addess, server_port, buffer_size):
        self.server_address = server_addess
        self.server_port = server_port
        self.buffer_size = buffer_size

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
    
    @property
    def request_bytes_to_send(self):
        return str.encode(self.request_content_string)

    @property
    def request_content_string(self) -> str:
        return json.dumps(self.request_content)
    
    @property
    def request_content(self) -> dict:
        return {
            'headers': self.headers,
            'body': self.body
        }

    @abstractmethod
    def send_request(self):
        pass

    @abstractmethod
    def get_response(self):
        pass
