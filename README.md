# GroupChat

## Description

&nbsp;Basic client-server chat system using Python's socket and threading libraries. It allows multiple clients to connect to a server and exchange messages, both public and private, with each other.

## Echo Client
1. Connection Setup:

* Connects to the server using IP 127.0.0.1 and port 5000.
* Prompts the user for a username and ensures it is available by communicating with the server.
  
2. Message Handling:

* Continuously receives messages from the server in a separate thread.
* Allows the user to send messages, which are sent to the server for distribution to other clients.
## Echo Server
1. Connection Management:

* Listens for incoming client connections on IP 127.0.0.1 and port 5000.
* Handles new client connections, ensuring each client has a unique username.
  
2. Message Processing:

* Forwards public messages to all clients.
* Handles private messages and special commands (e.g., listing all connected users).
## SocketWrapper Class
A utility class to manage socket communication, ensuring messages are correctly sent and received with a delimiter for message separation.

## Key Features:
* Concurrency: Utilizes threading to handle multiple clients simultaneously.
* Private Messaging: Supports sending private messages to specific users.
* Username Management: Ensures each client has a unique username.
* Dynamic Client List: Can list all connected users upon request.
  
This application provides a foundational structure for a real-time chat system, illustrating basic concepts in network programming and concurrent client handling.
