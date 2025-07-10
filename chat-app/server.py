import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = {}  # client_socket: username
rooms = {}    # room_name: list of client_sockets
client_rooms = {}  # client_socket: room_name

def broadcast(message, room, sender=None):
    for client in rooms.get(room, []):
        if client != sender:
            try:
                client.send(message.encode('utf-8'))
            except:
                pass

def handle_client(client):
    try:
        client.send("USERNAME".encode('utf-8'))
        username = client.recv(1024).decode('utf-8')
        clients[client] = username
        client.send("Type /join room_name to enter a room.".encode('utf-8'))

        while True:
            message = client.recv(1024).decode('utf-8')

            if message.startswith("/join "):
                room_name = message.split("/join ")[1]
                if client in client_rooms:
                    old_room = client_rooms[client]
                    rooms[old_room].remove(client)
                    broadcast(f"{clients[client]} left the room.", old_room, client)

                client_rooms[client] = room_name
                rooms.setdefault(room_name, []).append(client)
                broadcast(f"{clients[client]} joined the room.", room_name, client)
                client.send(f"Joined room {room_name}".encode('utf-8'))

            elif message.startswith("/exit"):
                if client in client_rooms:
                    room = client_rooms[client]
                    rooms[room].remove(client)
                    broadcast(f"{clients[client]} left the room.", room, client)
                client.send("Disconnected.".encode('utf-8'))
                client.close()
                del clients[client]
                break

            else:
                room = client_rooms.get(client)
                if room:
                    broadcast(f"{clients[client]}: {message}", room, client)
                else:
                    client.send("Join a room using /join room_name.".encode('utf-8'))

    except:
        client.close()
        if client in clients:
            del clients[client]

print(f"Server running on {HOST}:{PORT}...")
while True:
    client_socket, addr = server.accept()
    print(f"Connected: {addr}")
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()
