import os
import cv2
import numpy as np
import socket

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define server IP and port
ip = "192.168.43.147"
port = 8888

# Bind the socket
s.bind((ip, port))

# Listen for incoming connections
s.listen(5)

# Accept a connection
conn, addr = s.accept()

# Create a video capture object
cap = cv2.VideoCapture(1)

while True:
    data = conn.recv(90456)
    # Decode the image
    arry = np.fromstring(data, np.uint8)
    photo = cv2.imdecode(arry, cv2.IMREAD_COLOR)
    if type(photo) is type(None):
        pass
    else:
        cv2.imshow("SERVER-SCREEN", photo)
        if cv2.waitKey(10) == 13:
            break
    stat, photo = cap.read()
    # Encode the image and send it via the network
    photo_data = cv2.imencode('.jpg', photo)[1].tobytes()
    conn.sendall(photo_data)

cv2.destroyAllWindows()
cap.release()
os.system("cls")
