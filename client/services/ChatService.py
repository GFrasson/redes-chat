class ChatService:
    def __init__(self, client):
        self.client = client
        self.headers = {
            'path': '/message'
        }
        self.body = {
            'message': ''
        }
    
    def execute(self):
        client_message = input('Cliente: ')
        self.body['message'] = client_message
        
        response = self.client.get(self.body, self.headers)
        return response
