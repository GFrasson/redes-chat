from abc import ABC, abstractmethod


class BaseServer(ABC):
    def __init__(self, local_ip, local_port, buffer_size):
        self.local_ip = local_ip
        self.local_port = local_port
        self.buffer_size = buffer_size
        self.routes = {}

    def on(self, path, method):
        self.routes[path] = method

    def register_routes(self, routes):
        for path, method in routes.items():
            self.routes[path] = method

    def get_binded_method_from_path(self, path):
        return self.routes[path] or None

    def execute_binded_method(self, request):
        path = request['headers']['path']
        binded_method = self.get_binded_method_from_path(path)
        binded_method(request, self.response)
    
    @abstractmethod
    def listen(self):
        pass

    @abstractmethod
    def receive_request(self):
        pass
    
    @abstractmethod
    def response(self):
        pass