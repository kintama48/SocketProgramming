from socket import *

serverPort = 12002
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print(f'The server is listening on {serverPort}!')

connection_socket, addr = serverSocket.accept()

while True:
    print("Received Packet from:", connection_socket.getpeername())
    query = (connection_socket.recv(1024)).decode()

    # if the client does not wish to calculate again then
    # close connection
    if query in "qn":
        connection_socket.close()
        break

    query = query.split(", ")  # packet comes in form "{a}, {b}, {operation_type}" so split is needed

    # parse the list of strings got from query
    a, b = int(query[0]), int(query[1])
    operation = query[2]
    # ----------------------------------------

    result = 0

    if operation == "*":
        result = a * b
    elif operation == "/":
        result = a / b
    elif operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b

    connection_socket.send(str(result).encode())    # send result
