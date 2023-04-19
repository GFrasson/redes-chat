import socket
import json
from use_cases.Arithmetic import Arithmetic

class UDPServer:
    def __init__(self):
        self.local_ip = "127.0.0.1"
        self.local_port = 20001
        self.buffer_size = 1024
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.socket.bind((self.local_ip, self.local_port))

    def listen(self):
        return self.socket.recvfrom(self.buffer_size)



if __name__ == '__main__':
    server = UDPServer()
    
    print("Servidor UDP up e escutando...")

    # Escutando datagramas que chegam
    while True:
        request_encoded, address = server.listen()
        request_decoded = request_encoded.decode()
        
        request = json.loads(request_decoded)

        client_message = "Mensagem do Cliente: {}".format(request)
        client_ip = "Endereco IP do Cliente: {}".format(address)
        
        print(client_message)
        print(client_ip)

        first_number, second_number, operator = Arithmetic.get_elements_from_message(request_message)
        result = Arithmetic.arithmetic_operation(first_number, second_number, operator)
        
        response_message = str(result)
        response_bytes_to_send = str.encode(response_message)
        
        # Enviando msg de reply ao client
        server.socket.sendto(response_bytes_to_send, address)
