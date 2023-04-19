class ChatService:
    def __init__(self, client):
        self.client = client
        self.headers = {
            'path': '/message'
        }
        self.body = {
            'message': 'Mensagem para o servidor'
        }
    
    def execute(self):
        response = self.client.get(self.body, self.headers)
        return response
