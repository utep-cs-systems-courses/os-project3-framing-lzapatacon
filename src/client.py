import socket
import os
from src import *

HEADER = 64 #64 bytes
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'WARNING: Disconnecting from server...'

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)

def send():
    if f == DISCONNECT_MESSAGE:
        msg = msg.encode()
message_length = 
