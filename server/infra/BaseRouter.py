class BaseRouter():
    def __init__(self):
        self.routes = {}

    def on(self, path, method):
        self.routes[path] = method

    def register_routes(self, routes):
        for path, method in routes.items():
            self.routes[path] = method
    
    def get_binded_method_from_path(self, path):
        return self.routes[path] or None
