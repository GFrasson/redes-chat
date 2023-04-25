class ChatUseCase:
    def __init__(self) -> None:
        self.headers = {
            'path': '/message'
        }

    def execute(self, request, response):
        while True:
            server_message = input()
            print(f'\t\t\t{server_message} (SERVIDOR)')

            response({
                'headers': self.headers,
                'body': {
                    'message': server_message
                }
            })
