from providers.TCPClient import TCPClient
from services.ChatService import ChatService


if __name__ == '__main__':
    client = TCPClient()

    response = ChatService(client).execute()

    print("Mensagem vinda do Servidor {}".format(response))
