from gevent.server import StreamServer
from gevent.pool import Pool

def handle(socket, address):
    print socket.recv(1000)
    while True:
        import time
        print 'ha'
        time.sleep(1)

server = StreamServer(('localhost', 3000), handle, spwan=Pool(10))
server.serve_forever()
