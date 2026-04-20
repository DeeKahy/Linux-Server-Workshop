import socket
import threading
import sys

PORT = 9999

# Get server IP from command line, or ask for it
if len(sys.argv) > 1:
    HOST = sys.argv[1]
else:
    HOST = input("Server IP address: ").strip()

name = input("Your name: ").strip()
if not name:
    name = "Anonymous"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((HOST, PORT))
except ConnectionRefusedError:
    print(f"Could not connect to {HOST}:{PORT}")
    print("Make sure the server is running and the IP is correct.")
    sys.exit(1)

# Send our name as the first thing
sock.sendall((name + "\n").encode())

def receive_messages():
    """Run in a background thread — prints messages as they arrive."""
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("\n[Disconnected from server]")
                break
            print(data.decode(), end="", flush=True)
        except:
            break

receiver = threading.Thread(target=receive_messages)
receiver.daemon = True
receiver.start()

print("Connected! Type a message and press Enter. Ctrl+C to quit.\n")

try:
    while True:
        message = input()
        if message:
            sock.sendall((message + "\n").encode())
except KeyboardInterrupt:
    pass
finally:
    sock.close()
    print("Bye!")
