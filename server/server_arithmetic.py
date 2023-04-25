from providers.UDPServer import UDPServer
from use_cases.ArithmeticUseCase import ArithmeticUseCase


if __name__ == '__main__':
    server = UDPServer()

    server.router.on('/arithmetic', ArithmeticUseCase().execute)
    
    server.listen()
