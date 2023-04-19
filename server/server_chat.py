from providers.TCPServer import TCPServer


if __name__ == '__main__':
    server = TCPServer()

    server.listen()
