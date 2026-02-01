import socket
import time
import random

HOST = "localhost"
PORT = 9999

def start_socket_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print("🟢 Serveur socket démarré sur", HOST, PORT)
    conn, addr = server_socket.accept()
    print("🔗 Client connecté :", addr)

    # Lecture du fichier
    with open("data.txt", "r") as f:
        lines = f.readlines()

    # Envoi continu des messages
    while True:
        message = random.choice(lines).strip()
        conn.send((message + "\n").encode("utf-8"))
        print("📤 Envoyé :", message)
        time.sleep(2)

if __name__ == "__main__":
    start_socket_server()