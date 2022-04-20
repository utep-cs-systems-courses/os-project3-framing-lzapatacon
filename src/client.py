import socket
import os
from arc import *
HEADER = 64 #64 bytes
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MSG = 'WARnING: Disconnecting from server...'

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)

def send(msg):
    
    if msg = DISCONNECT_MSG
    if f == DISCONNECT_MESSAGE:
        msg = msg.encode()
    message_len = len(msg)
    send_len = str(message_length.encode(FORMAT))
    send_len += b' ' * (HEADER - len(send_length))
    client.send(send_len)
    client.send(msg)
    print(client.recv(2048).decode(FORMAT))
    
def send_name_of_file(file_name):
    return name_of_file
    
               
               
SEND_ANOTHER_FILE = True
while SEND_ANOTHER_FILE:
    path_of_text_file = input("\nThe name of the text file u want to send is: ")
    print("This is the text file you want to send:", path_of_text_file)

    if os.path.exists(path_oftext_file):
        
        encoded_file = archive_file(path_of_text_file)

        size_of_file = len(encoded_file)

        send(encoded_file)
    user_response = input("\nDo you want to send another file?) Y/N")
    if user_response == "Y":
        SEND_ANOTHER_FILE = True
    else:
        SEND_ANOTHER_FILE = False
        send(DISCONNECT_MESSAGE)
