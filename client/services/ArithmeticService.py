class ArithmeticService:
    def __init__(self, client):
        self.client = client
        self.headers = {
            'path': '/arithmetic'
        }
        self.body = {
            'first_number': 5,
            'second_number': 2,
            'operation': '/'
        }
    
    def execute(self):
        response = self.client.get(self.body, self.headers)
        return response
