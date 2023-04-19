from UDPServer import UDPServer
from use_cases.ArithmeticUseCase import ArithmeticUseCase


if __name__ == '__main__':
    server = UDPServer()

    server.register_routes({
        '/arithmetic': ArithmeticUseCase().execute
    })
    
    # Escutando datagramas que chegam
    while True:
        request = server.listen()
        print("Mensagem do Cliente: {}".format(request))

        path = request['headers']['path']
        use_case = server.get_method_from_path(path)
        use_case(request, server.response)
