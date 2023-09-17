import os
import cv2
import numpy as np
import socket

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define server IP and port
ip = "192.168.43.147"
port = 8888

# Connect to the server
s.connect((ip, port))

# Create a video capture object
cap = cv2.VideoCapture(0)

while True:
    stat, photo = cap.read()
    # Encode and send data via the network
    photo_data = cv2.imencode('.jpg', photo)[1].tobytes()
    s.sendall(photo_data)

    data = s.recv(90456)
    # Decode the image
    arry = np.fromstring(data, np.uint8)
    photo = cv2.imdecode(arry, cv2.IMREAD_COLOR)
    if type(photo) is type(None):
        pass
    else:
        cv2.imshow("CLIENT-SCREEN", photo)
        if cv2.waitKey(10) == 13:
            break

cv2.destroyAllWindows()
cap.release()
os.system("cls")
