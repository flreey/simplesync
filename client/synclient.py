from gevent.socket import socket

sock = socket()
sock.connect(('localhost', 3000))
sock.send('haha')
print sock.recv(1000)
