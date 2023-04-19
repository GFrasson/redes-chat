import socket
import json

class UDPClient:
    def __init__(self):
        self.address = "127.0.0.1"
        self.port = 20001
        self.buffer_size = 1024
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.headers = {
            'path': '/'
        }
        self.payload = {
            'body': {},
        }

    def send_request(self):
        request_content = self.get_request_content_string()
        request_bytes_to_send = str.encode(request_content)

        self.socket.sendto(request_bytes_to_send, (self.address, self.port))

    def get_request_content_string() -> str:
        return json.dumps({
            'headers': self.headers,
            'payload': self.payload
        })

    def get(self, message: str, path: str = '/teste'):
        self.headers['path'] = path
        self.payload['body'] = message        

        self.send_request()

        return self.socket.recvfrom(self.buffer_size)

def prepare_arithmetic_operation_message(a: int | float, b: int | float, operation: str) -> str:
    return f'{a} {operation} {b}'

if __name__ == '__main__':
    message = prepare_arithmetic_operation_message(5, 2, '/')
    
    client = UDPClient()

    response = client.get(message)

    response_message = "Mensagem vinda do Servidor {}".format(response[0])
    print(response_message)
