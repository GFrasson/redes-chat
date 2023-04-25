from threading import Thread
from abc import ABC, abstractmethod

from infra.BaseRouter import BaseRouter


class BaseServer(ABC):
    def __init__(self, local_ip, local_port, buffer_size):
        self.local_ip = local_ip
        self.local_port = local_port
        self.buffer_size = buffer_size
        
        self.router = BaseRouter()

        self.listener_threads = []
        self.worker_threads = []
        self.create_listener_thread()
    
    def create_worker_thread(self, request):
        if len(self.worker_threads) > 0 and self.worker_threads[0].is_alive():
            return self.worker_threads[0]
        
        worker_thread = Thread(target=self.execute_binded_method, args=(request, self.response))
        self.worker_threads.append(worker_thread)

        return worker_thread
    
    def create_listener_thread(self):
        listener_thread = Thread(target=self.thread_listen)
        self.listener_threads.append(listener_thread)

        return listener_thread
    
    def listen(self):
        for listener_thread in self.listener_threads:
            listener_thread.start()

    def execute_binded_method(self, request, response):
        path = request['headers']['path']
        binded_method = self.router.get_binded_method_from_path(path)
        binded_method(request, response)

    @abstractmethod
    def thread_listen(self):
        pass

    @abstractmethod
    def receive_request(self):
        pass
    
    @abstractmethod
    def response(self):
        pass
