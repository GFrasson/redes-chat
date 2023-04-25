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
    
    def receive(self):
        data_received_encoded = self.socket.recv(self.buffer_size)
        data_received_decoded = data_received_encoded.decode()

        if not data_received_decoded:
            return None

        return json.loads(data_received_decoded)
    
    def thread_listen(self):
        while True:
            data_received = self.receive()
            
            if data_received is None:
                continue

            message = data_received['body']['message']
            print('(SERVIDOR) ', message)

            worker = self.create_worker_thread(data_received)
            if not worker.is_alive:
                worker.start()
