from providers.UDPClient import UDPClient
from services.ArithmeticService import ArithmeticService


if __name__ == '__main__':
    client = UDPClient()

    response = ArithmeticService(client).execute()

    print("Mensagem vinda do Servidor {}".format(response))
