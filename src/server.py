import socket
import os
import threading
from arc import *

port = 5050

HEADER = 64

SERVER = socket.gethostbyname(socket.gethostname())

print("This is the name of my local device: ", socket.gethostname())
print("This is the ip adress: ", SERVER)

ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT from server..."

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)

def handle_client(connection, address):
    print(f"[NEW CONNECTION] {address} connected.")

    connected = True
    file_counter = 0

    while connected:

        message_length = connection.recv(HEADER).decode(FORMAT)

        if message_length:
            message_length = int(message_length)

            message_length = connection.recv(message_length).decode(FORMAT)

            file_counter += 1

            name_of_new_file = "RECIEVED FILE" +  "_" + "[" + str(address) + "] " + str(file_counter) + ".txt"
            unarchive_file(name_of_new_file, message)

            if message ==  DISCONNECT_MESSAGE:
                connected = False

            print(f"\n[{address}] {message}")
            connection.send("Message received.".encode(FORMAT))
    connection.close()

def start():

    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:

        connection, address = server.accept()

        thread = threading.Thread(target = handle_client, args=(connection, address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("\n[STARTING] server is starting")
start()
