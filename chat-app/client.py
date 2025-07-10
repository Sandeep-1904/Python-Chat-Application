import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Disconnected from server.")
            client.close()
            break

def write():
    while True:
        msg = input("")
        if msg.startswith("/exit"):
            client.send("/exit".encode('utf-8'))
            break
        else:
            client.send(msg.encode('utf-8'))

username = input("Enter your username: ")

def init_connection():
    while True:
        msg = client.recv(1024).decode('utf-8')
        if msg == "USERNAME":
            client.send(username.encode('utf-8'))
        else:
            print(msg)
            break

init_connection()

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
