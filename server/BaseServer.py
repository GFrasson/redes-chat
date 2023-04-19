class BaseServer:
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

    def get_method_from_path(self, path):
        return self.routes[path] or None
