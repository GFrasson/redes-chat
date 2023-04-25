from providers.TCPServer import TCPServer
from use_cases.ChatUseCase import ChatUseCase


if __name__ == '__main__':
    server = TCPServer()

    server.router.on('/message', ChatUseCase().execute)

    server.listen()
