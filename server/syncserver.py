import gevent
from gevent import spawn, sleep
from gevent.server import StreamServer
from gevent.pool import Pool

def handle(socket, address):
    print socket.recv(1000)
    contents = readfile()
    socket.send(contents)
    #spawn(p)
    #gevent.joinall([spawn(p)], 0)
    #sleep(0)

def readfile():
    import glob
    fs = glob.glob('*')
    contents = ''
    for f in fs:
        with open(f, 'r') as ff:
            contents += contents.join(ff.readlines())

    print contents
    return contents

pool = Pool(1000)
server = StreamServer(('localhost', 3000), handle, spawn=pool)
server.serve_forever()
