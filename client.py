from socket import *
from utils import *     # importing util functions from utils.py

server_name = '192.168.43.70'  # Please enter your IP here
server_port = 12002
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))

print(client_socket.getsockname())

user_input = get_input()    # takes input from user (defined in utils.py)

while True:

    # checks if user wants to quit by entering "q"
    if not is_digit(user_input) and user_input.lower().strip() in "q":
        client_socket.send("q".encode())
        break

    # checks if entered option is a digit and is less than 4 and greater than 1
    elif not is_digit(user_input) or \
            (is_digit(user_input) and (1 > int(user_input) or int(user_input) > 4)):
        print("\n      ERROR: Please Enter a Valid Option!")
        user_input = get_input()
        continue
    else:
        selected_option = int(user_input)
        a, b = get_numerical_input()        # takes a & b from user

        # concatenates a string that'll be encoded and sent to server
        # for processing
        if selected_option == 1:
            query = f"{a}, {b}, *"
        elif selected_option == 2:
            query = f"{a}, {b}, -"
        elif selected_option == 3:
            query = f"{a}, {b}, /"
        else:
            query = f"{a}, {b}, +"

    # sends a, b & operation_type to server in str form
    client_socket.send(query.encode())

    # decodes server results
    result = client_socket.recv(1024).decode()

    print_result(result)

    again = search_again()

    # if search_again is "n"
    # then tell server to close connection and close client connection
    # else continue
    if again.lower().strip() == 'n':
        client_socket.send(again.lower().encode())
        break
    else:   # take input again if user enters 'y' or anything else
        user_input = get_input()

client_socket.close()
