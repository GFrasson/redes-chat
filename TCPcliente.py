import socket


# Cria socket do cliente TCP
echoClient =  socket.socket();


# Nota: Nao precisa de bind() para sockets client...
# Eh so chamar connect()
echoClient.connect(("127.0.0.1", 32007));
 

# Envia uma msg
echoClient.send("Enviando mensagem do cliente TCP".encode());

# Pega o retorno do servidor
msgReceived = echoClient.recv(1024);


# imprime retorno e fecha
print("Msg recebida no cliente: %s"%msgReceived.decode());