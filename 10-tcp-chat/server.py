import socket
import threading

PORT = 9999

# Keep track of everyone connected: {socket: name}
clients = {}
lock = threading.Lock()

def broadcast(message, exclude=None):
    """Send a message to everyone except the sender."""
    with lock:
        for client in list(clients):
            if client == exclude:
                continue
            try:
                client.sendall(message.encode())
            except:
                client.close()
                del clients[client]

def handle_client(conn, addr):
    try:
        # First message the client sends is their name
        name = conn.recv(1024).decode().strip()
        if not name:
            conn.close()
            return

        with lock:
            clients[conn] = name

        print(f"+ {name} connected ({addr[0]})")
        broadcast(f">> {name} joined the chat\n", exclude=conn)
        conn.sendall(f"Welcome {name}! There are {len(clients)} people here.\n".encode())

        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode().strip()
            if message:
                print(f"{name}: {message}")
                broadcast(f"{name}: {message}\n", exclude=conn)

    except (ConnectionResetError, BrokenPipeError):
        pass
    finally:
        with lock:
            name = clients.pop(conn, "someone")
        conn.close()
        print(f"- {name} disconnected")
        broadcast(f">> {name} left the chat\n")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("0.0.0.0", PORT))
server.listen()

print(f"Chat server running on port {PORT}")
print(f"Others can connect with:  python3 client.py YOUR_SERVER_IP")
print(f"Waiting for connections...\n")

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.daemon = True
    thread.start()
