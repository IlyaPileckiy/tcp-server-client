import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)

server_socket.bind(("127.0.0.1", 53210))  # default TCP port.

server_socket.listen(1000)  # backlog определяет размер очереди для установленных, но еще не обработанных программой соединений
# server socket находится в состоянии LISTEN - готов принимать входящие соединения

# client_socket, client_addr = server_socket.accept()
# clent socket находится в состоянии ESTABLISHED - готов к приему и передаче данных
print("Server is ready")

while True:
    # Бесконечно обрабатываем входящие подключения
    client_socket, client_addr = server_socket.accept()
    print("Connected by", client_addr)

    while True:
        # Пока клиент не отключился, читаем передаваемые им данные и отправляем их обратно
        data = client_socket.recv(1024)
        if not data:
            # Клиент отключился
            break
        client_socket.sendall(data)
        print(data)

    client_socket.close()
    print("Connection closed")
