import socket
import json


class UDPServer:
    def __init__(self):
        self.local_ip = "127.0.0.1"
        self.local_port = 20001
        self.buffer_size = 1024
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.socket.bind((self.local_ip, self.local_port))
        print("Servidor UDP up e escutando...")
    
        self.routes = {}

    def listen(self):
        while True:
            request = self.receive_request()
            print("Mensagem do Cliente: {}".format(request))

            path = request['headers']['path']
            method = self.get_method_from_path(path)
            method(request, self.response)

    def receive_request(self):
        request_encoded, address = self.socket.recvfrom(self.buffer_size)
        self.client_address = address

        request_decoded = request_encoded.decode()
        request = json.loads(request_decoded)

        return request
    
    def response(self, body: dict):
        response_body = json.dumps(body)
        response_body_encoded = str.encode(response_body)

        self.socket.sendto(response_body_encoded, self.client_address)

    def on(self, path, method):
        self.routes[path] = method

    def register_routes(self, routes):
        for path, method in routes.items():
            self.routes[path] = method

    def get_method_from_path(self, path):
        return self.routes[path] or None
