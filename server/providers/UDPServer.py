import socket
import json

from providers.BaseServer import BaseServer


class UDPServer(BaseServer):
    def __init__(self):
        super().__init__(local_ip="127.0.0.1", local_port=20001, buffer_size=1024)

        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.socket.bind((self.local_ip, self.local_port))
        print("Servidor UDP up e escutando...")

    def thread_listen(self):
        while True:
            request = self.receive_request()
            print("Mensagem do Cliente: {}".format(request))

            worker = self.create_worker_thread(request)
            if not worker.is_alive():
                worker.start()

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
