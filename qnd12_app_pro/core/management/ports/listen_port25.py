# description: python 3 socket server printing and echoing received data
import socket
import sys

# host: all available interfaces
host = ''
# port: set to port 25 for our test
port = 25
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket created')
try:
	s.bind((host, port))
except socket.error as msg:
	print('bind failed, msg = {}'.format(msg))
	sys.exit()
print('bind done')

s.listen(1)
print('start listening')

conn, addr = s.accept()
print('Connection from ', addr)
while True:
    data = conn.recv(1024)
    print('data = {}'.format(data))
    if not data: 
        break
    conn.sendall(data)
conn.close()