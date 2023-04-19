import socket


# servidor de echo simples com TCP
echoSocket = socket.socket();


# Fazer a associacao (bind) de numero IP e numero de porta
echoSocket.bind(("127.0.0.1", 32007));

# Escutando conexoes que vao chegar
echoSocket.listen();


# Inicia o aceite de 1 novo cliente

while(True):
    (clientSocket, clientAddress) = echoSocket.accept();

    # Tratando 1 requisicao de 1 cliente
    while(True):
        data = clientSocket.recv(1024);
        print("Recebi no servidor a msg: %s"%data);

        if(data!=b''):
            # Simplesmente envia de volta o que recebeu
            clientSocket.send(data);
            break;