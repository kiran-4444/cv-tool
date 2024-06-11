import asyncio
import sys

import pyperclip
import websockets

from nmap_scan import get_host_ip_address

if sys.argv[1] == "client":

    async def send_message():
        uri = "ws://192.168.0.12:8765"  # Replace <server_ip> with the IP address of the server
        async with websockets.connect(uri) as websocket:
            while True:
                message = input("Enter message to send: ")
                await websocket.send(message)
                response = await websocket.recv()
                print(f"Received response: {response}")
                pyperclip.copy(response)

    asyncio.get_event_loop().run_until_complete(send_message())

elif sys.argv[1] == "server":

    async def handler(websocket, path):
        print("Client connected")
        try:
            previous_clipboard_content = None
            async for message in websocket:
                if pyperclip.paste() != previous_clipboard_content:
                    print(f"Received message: {message}")
                    pyperclip.copy(message)
                    previous_clipboard_content = message
                    response = message
                    await websocket.send(response)
        except websockets.ConnectionClosed as e:
            print("Connection closed", e)

    start_server = websockets.serve(handler, "0.0.0.0", 8765)

    asyncio.get_event_loop().run_until_complete(start_server)
    print("Server started on ws://0.0.0.0:8765")
    asyncio.get_event_loop().run_forever()
