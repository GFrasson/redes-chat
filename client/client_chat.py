from providers.TCPClient import TCPClient
from services.ChatService import ChatService


if __name__ == '__main__':
    client = TCPClient()

    client.router.on('/message', lambda response: ChatService(client).execute())

    client.listen()

    ChatService(client).execute()
