import json
from threading import Thread
from abc import ABC, abstractmethod

from infra.BaseRouter import BaseRouter


class BaseClient(ABC):
    def __init__(self, server_addess, server_port, buffer_size):
        self.server_address = server_addess
        self.server_port = server_port
        self.buffer_size = buffer_size

        self.headers = {
            'path': '/'
        }
        self.body = {}

        self.router = BaseRouter()

        self.worker_threads = []
        self.listener_threads = []
        self.create_listener_thread()
    
    def get(self, body: dict, headers: dict[str, str] = {}):
        self.prepare_request_content(body, headers)        
        self.send_request()

        response = self.receive()
        return response

    def prepare_request_content(self, body: dict, headers: dict[str, str] = {}):
        for key, value in body.items():
            self.body[key] = value
        
        for key, value in headers.items():
            self.headers[key] = value

    def listen(self):
        for listener_thread in self.listener_threads:
            listener_thread.start()

    def create_worker_thread(self, response):
        if len(self.worker_threads) > 0 and self.worker_threads[0].is_alive():
            return self.worker_threads[0]
        
        worker_thread = Thread(target=self.execute_binded_method, args=(response,))
        self.worker_threads.append(worker_thread)
        
        return worker_thread
    
    def create_listener_thread(self):
        listener_thread = Thread(target=self.thread_listen)
        self.listener_threads.append(listener_thread)

        return listener_thread
    
    def execute_binded_method(self, response):
        path = response['headers']['path']
        binded_method = self.router.get_binded_method_from_path(path)
        binded_method(response)
    
    @property
    def request_bytes_to_send(self):
        return str.encode(self.request_content_string)

    @property
    def request_content_string(self) -> str:
        return json.dumps(self.request_content)
    
    @property
    def request_content(self) -> dict:
        return {
            'headers': self.headers,
            'body': self.body
        }
    
    @abstractmethod
    def thread_listen(self):
        pass

    @abstractmethod
    def send_request(self):
        pass

    @abstractmethod
    def receive(self):
        pass
