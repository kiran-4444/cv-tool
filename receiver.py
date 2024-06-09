import socket

import pyperclip

from nmap_scan import get_host_ip_address


def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Received: {data.decode()}")
        pyperclip.copy(data.decode())

    conn.close()


if __name__ == "__main__":
    current_host_ip = get_host_ip_address()
    host = current_host_ip  # Host IP address
    PORT = 65432  # Port to listen on
    start_server(host, PORT)
