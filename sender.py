import socket
import sys

import pyperclip

from nmap_scan import get_ip_from_mac


def start_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")

    try:
        previous_clipboard_content = None
        while True:
            if pyperclip.paste() != previous_clipboard_content:
                message = pyperclip.paste()
                client_socket.sendall(message.encode())
                pyperclip.copy("")
                print(f"Sent: {message}")
                previous_clipboard_content = message
    finally:
        client_socket.close()


if __name__ == "__main__":
    destination_mac_address = sys.argv[1].upper()
    destination_ip_address = get_ip_from_mac(destination_mac_address)
    PORT = 65432  # Server's port
    start_client(destination_ip_address, PORT)
