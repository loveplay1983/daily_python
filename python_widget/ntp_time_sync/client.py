import subprocess
import socket
import time
import sys
import struct

SERVER_HOST = '192.168.1.100'
SERVER_PORT = 37123
BUF_SIZE = 1024

def client(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    message = struct.pack('>2b8s', 3, 7, 'get_time')

    try:
        sock.sendall(message)
        response = sock.recv(BUF_SIZE)
        i1, i2, cur_time = struct.unpack('!2bi', response)
        formattime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(cur_time)))
        ret = subprocess.call(''' date -s "%s" ''' % formattime, shell=True)
        print "client received: %s format: %s" % (response, formattime)
    except Exception, e:
        print "error: " + str(e)
        sys.exit(2)
    else:
        sock.close()
        return ret

if __name__ == "__main__":
    client(SERVER_HOST, SERVER_PORT)
