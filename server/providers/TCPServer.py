import socket
import json

from providers.BaseServer import BaseServer


class TCPServer(BaseServer):
    def __init__(self):
        super().__init__(local_ip="127.0.0.1", local_port=32007, buffer_size=1024)

        self.socket = socket.socket()
        self.socket.bind((self.local_ip, self.local_port))
        self.socket.listen()
        print("Servidor TCP up e escutando...")

    def accept_client(self):
        client_socket, client_address = self.socket.accept()
        self.client_socket = client_socket
        self.client_address = client_address
    
    def listen(self):
        while True:
            self.accept_client()

            # Tratando 1 requisicao de 1 cliente
            while True:
                request = self.receive_request()
                print("Mensagem do Cliente: {}".format(request))

                self.execute_binded_method(request)

                # if request != b'':
                #     self.response({
                #         'message': 'mensagem de volta'
                #     })
                #     # self.client_socket.send(request)
                #     break

        # request_encoded, address = self.socket.recvfrom(self.buffer_size)
        # self.client_address = address

        # request_decoded = request_encoded.decode()
        # request = json.loads(request_decoded)

        # return request

    def receive_request(self):
        request_encoded = self.socket.recvfrom(self.buffer_size)
        request_decoded = request_encoded.decode()
        request = json.loads(request_decoded)

        return request
    
    def response(self, body: dict):
        response_body = json.dumps(body)
        response_body_encoded = str.encode(response_body)

        self.client_socket.send(response_body_encoded)
