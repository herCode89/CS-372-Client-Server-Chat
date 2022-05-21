import socket
import sys

Host = '127.0.0.1'
Port = 57700

connStart = True

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create an INET, STREAM socket
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Socket reuse option from PDF
sock.bind((Host, Port))  # Bind socket to Host and Port
sock.listen(1)
print(f"Server listening on: localhost on port: {Port}")
communicate = False
connection, address = sock.accept()  # Accept the connection
print(f"Connected by: {address}")
print("Waiting for message...")

while True:  # Loop till /q is entered by client
    receivedMSG = connection.recv(10)
    listened = connection.recv(int(receivedMSG.decode('UTF-8'.strip())))
    listened = listened.decode()

    if listened:  # Continue if client responded
        if not listened != "/q":  # quit
            connection.close()  # close
            sys.exit()  # exit

        else:
            print(listened)  # messaged printed

        if not communicate:
            print("Type /q to quit")  # To quit chat
            print("Enter message to send...")  # Prompt to send message back
            communicate = True
        talk = input(">")  # To show where to input response if responding
        talk = talk.encode('UTF-8')  # To encode response to send
        sendMSG = (f"{len(talk):<10}".encode('UTF-8'))  # Give header with information
        connection.send(sendMSG + talk)  # Send response


