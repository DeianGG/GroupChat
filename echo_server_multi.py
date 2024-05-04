import socket
import threading
import json
import echo_protocol as echo
 
print("Welcome to Echo Server!")

IP = '127.0.0.1'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((IP, echo.PORT))
sock.listen()

clienti = []

def handle_client(client_socket, client_address, username):
    global clienti
    print(f"Thread for handling client: {client_address}")
    sock_wrapper = echo.SocketWrapper(client_socket)
    try:
        while True:
            rcvd = sock_wrapper.recv_msg()
            if rcvd is None:
                client_sock.close()
                break
            if rcvd[0] == "/":
                print(rcvd)
                if rcvd[1:4] == "msg":
                    if len(rcvd) > 5:
                        to = rcvd.split(' ')[1]
                        final = "PRIVATE " + username + ":" + rcvd[(5+len(to)):]
                        for client in clienti:
                            if client[1] == to:
                                client[0].send_msg(final)
                elif rcvd[1:2] == "l":
                    for client in clienti:
                        if client[1] == username:
                            usernames = []
                            for c in clienti:
                                usernames.append(c[1])
                            sock_wrapper.send_msg(json.dumps(usernames))
            else:
                rcvd = username+": "+rcvd
                for client in clienti:
                    if client[0].sock != sock_wrapper.sock:
                        client[0].send_msg(rcvd)
    except Exception as e:
        print(f"An error occurred with the client at {client_address}: {e}")
    finally:
        clienti = [client for client in clienti if client[0].sock != sock_wrapper.sock]
        client_socket.close()
 
while True:
    print("Ready to accept a client connection.")
    client_sock, addr = sock.accept()
    client = echo.SocketWrapper(client_sock)
    username = client.recv_msg()
    valabil = True
    for c in clienti:
        if c[1] == username:
            valabil = False
    while valabil == False:
        client.send_msg(json.dumps({'type': 'unavailable_username'}))
        username = client.recv_msg()
        valabil = True
        for c in clienti:
            if c[1] == username:
                valabil = False
    client.send_msg(json.dumps({'type': 'available_username'}))
    clienti.append((client, username))
    print(f"Accepted new client connection: {addr}")
    th = threading.Thread(target=handle_client, args=(client_sock, addr, username), daemon=True)
    th.start()