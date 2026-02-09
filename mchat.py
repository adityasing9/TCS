import socket
import threading
import sys

HOST = ''
PORT = 5000

clients = []
running = True

def handle_client(conn, addr):
    global running
    print(f"[+] {addr} joined")
    try:
        conn.send("Welcome to the chat!\n".encode())
        while running:
            msg = conn.recv(1024)
            if not msg:
                break
            message = msg.decode().strip()
            print(f"{addr}: {message}")
            broadcast(f"{addr}: {message}\n", conn)
    except:
        pass
    finally:
        if conn in clients:
            clients.remove(conn)
        conn.close()
        print(f"[-] {addr} left")

def broadcast(message, sender=None):
    for client in clients[:]:
        try:
            if client != sender:
                client.send(message.encode())
        except:
            clients.remove(client)

def server_input():
    global running
    while running:
        try:
            msg = input("Server: ")
        except EOFError:
            break

        if msg.lower() == "exit":
            print("Shutting down server...")
            running = False
            break

        broadcast(f"Server: {msg}\n")

def start_server():
    global running
    server = socket.socket()
    server.bind((HOST, PORT))
    server.listen()

    print(f"[+] Chat server started on port {PORT}")

    threading.Thread(target=server_input, daemon=True).start()

    try:
        while running:
            server.settimeout(1)
            try:
                conn, addr = server.accept()
                clients.append(conn)
                threading.Thread(
                    target=handle_client,
                    args=(conn, addr),
                    daemon=True
                ).start()
            except socket.timeout:
                continue
    finally:
        print("[*] Closing server...")
        for c in clients:
            c.close()
        server.close()
        sys.exit(0)

start_server()
