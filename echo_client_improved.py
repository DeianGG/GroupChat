import json
import socket
import threading
import echo_protocol as echo
 
IP = '127.0.0.1'
PORT = 5000
 
print("Welcome to Echo Client!")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP, PORT))

sock_wrapper = echo.SocketWrapper(sock)

username = input("Username: ")
sock_wrapper.send_msg(username)
msg = sock_wrapper.recv_msg()
while json.loads(msg)['type'] == 'unavailable_username':
    username = input("Enter another username: ")
    sock_wrapper.send_msg(username)
    msg = sock_wrapper.recv_msg()   
def recv_messages(sock_wrapper):
    while True:
        rec = sock_wrapper.recv_msg()
        print(rec)

th = threading.Thread(target=recv_messages, args=(sock_wrapper,), daemon=True)
th.start()
while True:
    msg = input()
    sock_wrapper.send_msg(msg)
            


sock.close()