import socket
import sys

Host = '127.0.0.1'
Port = 57700

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create an INET, STREAM socket
sock.connect((Host, Port))  # Connect socket to Host and Port
print(f"Connected to: localhost on port: {Port}")
print("Type /q to quit")
print("Enter message to send...")

while True:  # Loop till /q
    talk = input(">")  # To show where to input response if responding
    talk = talk.encode('UTF-8')  # To encode response to send
    sendMSG = (f'{len(talk):<10}'.encode('UTF-8'))
    sock.send(sendMSG + talk)

    if not talk.decode() != "/q":  # quit
        sock.close()  # close
        sys.exit()  # exit

    receivedMSG = sock.recv(10)  # Received response
    gotMSG = sock.recv(int(receivedMSG.decode('UTF-8'.strip())))  # Decode, convert to read response
    gotMSG = gotMSG.decode()  # Decode response

    print(gotMSG)
