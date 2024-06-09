import socket
import sys

from nmap_scan import get_ip_from_mac


def start_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")

    try:
        while True:
            message = input("Enter message to send: ")
            client_socket.sendall(message.encode())
            if message.lower() == "exit":
                print("Exiting...")
                break
    finally:
        client_socket.close()


if __name__ == "__main__":
    destination_mac_address = sys.argv[1].upper()
    destination_ip_address = get_ip_from_mac(destination_mac_address)
    PORT = 65432  # Server's port
    start_client(destination_ip_address, PORT)
