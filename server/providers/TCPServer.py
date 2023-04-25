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
    
    def thread_listen(self):
        while True:
            self.accept_client()

            while True:
                request = self.receive_request()
                
                if request is None:
                    continue

                message = request['body']['message']
                print('(CLIENTE) ', message)

                # TODO: Create one worker thread for each client accepted and map an identifier
                worker = self.create_worker_thread(request)
                if not worker.is_alive():
                    worker.start()

    def receive_request(self):
        request_encoded = self.client_socket.recv(self.buffer_size)
        request_decoded = request_encoded.decode()

        if not request_decoded:
            return None

        request = json.loads(request_decoded)
        return request
    
    def response(self, data: dict):
        response_data = json.dumps(data)
        response_data_encoded = str.encode(response_data)

        self.client_socket.send(response_data_encoded)
