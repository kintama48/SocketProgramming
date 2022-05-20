from socket import *
from utils import *

server_name = '192.168.43.70'  # 'servername'
server_port = 12002
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))
print(client_socket.getsockname())

user_input = get_input()

while True:
    if not is_digit(user_input) and user_input.lower().strip() in "q":
        client_socket.send("q".encode())
        break
    elif not is_digit(user_input) or (is_digit(user_input) and 1 > int(user_input) > 4):
        print("      ERROR: Please Enter a Valid Option!")
        user_input = get_input()
        continue
    else:
        selected_option = int(user_input)
        a, b = get_numerical_input()

        if selected_option == 1:
            query = f"{a}, {b}, *"
        elif selected_option == 2:
            query = f"{a}, {b}, -"
        elif selected_option == 3:
            query = f"{a}, {b}, /"
        else:
            query = f"{a}, {b}, +"

    client_socket.send(query.encode())
    result = client_socket.recv(1024).decode()

    print_result(result)

    again = search_again()

    # If search again is "n"
    # Then tell server to close connection and close client Connection

    if again.lower().strip() == 'n':
        client_socket.send(again.lower().encode())
        break

client_socket.close()
