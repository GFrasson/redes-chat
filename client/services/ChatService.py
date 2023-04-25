from providers.BaseClient import BaseClient


class ChatService:
    def __init__(self, client: BaseClient):
        self.client = client
        self.headers = {
            'path': '/message'
        }
        self.body = {
            'message': ''
        }
    
    def execute(self):
        while True:
            client_message = input()
            print(f'\t\t\t{client_message} (CLIENTE)')
            self.body['message'] = client_message
            
            self.client.prepare_request_content(self.body, self.headers)
            self.client.send_request()
