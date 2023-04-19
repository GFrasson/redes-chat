class ChatUseCase:
    def execute(self, request, response):
        message = request['body']['message']

        print('Cliente:', message)

        server_message = input('Servidor:')

        response({
            'message': server_message
        })
