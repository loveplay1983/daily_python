https://code.tutsplus.com/tutorials/introduction-to-network-programming-in-python--cms-30459


This tutorial will give an introduction to sockets in Python and how to use the socket module to build HTTP servers and clients in Python. It will also cover Tornado, a Python networking library which is ideal for long polling, WebSockets, and other applications that require a long-lived connection to each user.

What Are Sockets?
A socket is a link between two applications that can communicate with one another (either locally on a single machine or remotely between two machines in separate locations).

Basically, sockets act as a communication link between two entities, i.e. a server and a client. A server will give out information being requested by a client. For example, when you visited this page, the browser created a socket and connected to the server.

The socket Module
In order to create a socket, you use the socket.socket() function, and the syntax is as simple as:

1
2
import socket
s= socket.socket (socket_family, socket_type, protocol=0)
Here is the description of the arguments:

socket_family: Represents the address (and protocol) family. It can be either AF_UNIX or AF_INET.
socket_type: Represents the socket type, and can be either SOCK_STREAM or SOCK_DGRAM.
protocol: This is an optional argument, and it usually defaults to 0.
After obtaining your socket object, you can then create a server or client as desired using the methods available in the socket module.

Create a Simple Client
Before we get started, let's look at the client socket methods available in Python.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(): Initiates a TCP server connection.
To create a new socket, you first import the socket method of the socket class.

1
import socket
Next, we'll create a stream (TCP) socket as follows:

1
stream_socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
The AF_INET argument indicates that you're requesting an Internet Protocol (IP) socket, specifically IPv4. The second argument is the transport protocol type SOCK_STREAM for TCP sockets. Additionally, you can also create an IPv6 socket by specifying the socket AF_INET6 argument.

Specify the server.

1
server = "localhost"
Specify the port we want to communicate with.

1
port =80
Connect the socket to the port where the server is listening.

1
2
server_address = ((host, port))
stream_socket.connect(server_address)
It's important to note that the host and port must be a tuple.

Send a data request to the server:

1
2
message = 'message'
stream_socket.sendall(message)
Get the response from the server:

1
2
data = sock.recv(10)
print data
To close a connected socket, you use the close method:

1
stream_socket.close()
Below is the full code for the Client/Server.

01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
import socket
import sys

# Create a TCP/IP socket
stream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define host
host = 'localhost'

# define the communication port
port = 8080

# Connect the socket to the port where the server is listening
server_address = ((host, port))

print "connecting"

stream_socket.connect(server_address)


# Send data
message = 'message'
stream_socket.sendall(message)

# response
data = stream_socket.recv(10)
print data


print 'socket closed'
stream_socket.close()
Build a Simple Server
Now let's take a look at a simple Python server. The following are the socket server methods available in Python.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(): Binds address (hostname, port number) to socket.
s.listen(): Sets up and starts TCP listener.
s.accept(): Accepts TCP client connection.
We will follow the following steps:  

Create a socket.
Bind the socket to a port.
Start accepting connections on the socket.
Here is the server program.

01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define host
host = 'localhost'

# define the communication port
port = 8080

# Bind the socket to the port
sock.bind((host, port))
# Listen for incoming connections
sock.listen(1)

# Wait for a connection
print 'waiting for a connection'
connection, client = sock.accept()

print client, 'connected'

# Receive the data in small chunks and retransmit it

data = connection.recv(16)
print 'received "%s"' % data
if data:

    connection.sendall(data)
else:
    print 'no data from', client


# Close the connection
connection.close()
The server is now ready for incoming connections.

Now run the client and server programs in separate terminal windows, so they can communicate with each other.

Server Output
1
2
3
4
$ python server.py
waiting for a connection
('127.0.0.1', 47050) connected
received "message"
Client Output
1
2
3
4
$ python client.py
connecting
message
socket closed
The Tornado Framework
The Tornado framework is one of the libraries available for network programming in Python. In this section, we will discuss this library and show how to use it to build WebSockets.

Tornado is a Python web framework and asynchronous networking library. Tornado uses the non-blocking network I/O, and hence is capable of scaling to tens of thousands of open connections. This trait makes it ideal for long polling, WebSockets, and other applications that require a long-lived connection to each user.

Let's create a simple Tornado WebSocket:

01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
import tornado.ioloop
import tornado.web


class ApplicationHandler(tornado.web.RequestHandler):

    def get(self):
        self.message = message = """<html>
<head>
    <title>Tornado Framework</title>

</head>
<body
    <h2>Welcome to the Tornado framework</h2>
</body>
</html>"""
        self.write(message)


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", ApplicationHandler),
    ])
    application.listen(5001)
    tornado.ioloop.IOLoop.instance().start()
In the code above:

We define the class ApplicationHandler which serves as the handler for a request and returns a response using the write() method.
The main method is the entry for the program.
tornado.web.Application creates a base for the web application and takes a collection of handlers, i.e. ApplicationHandler.
The Application listens on port 5000, and a client can communicate to this application using the same port.
tornado.ioloop.IOLoop.instance().start() creates a nonblocking thread for an application.
If we run the application, we will get the result as shown in the screenshot below.

The results of running our application
Conclusion
By now you must have grasped the basics of socket programming in Python and how you can build a simple server and client. Feel free to experiment by building your own chat client. For more information, visit the official Python docs.

Additionally, don’t hesitate to see what we have available for sale and for study in the Envato Market, and don't hesitate to ask any questions and provide your valuable feedback using the feed below.
