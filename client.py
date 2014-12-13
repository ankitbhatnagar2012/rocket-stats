'''
Sample client to push data to a UDP server
'''
import socket
import sys

SERVER_HOST = 'localhost'
SERVER_PORT = 5000

try:
	_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print 'Socket generated successfully'
except socket.error, msg:
	print 'Failed to generate a socket. Error : ' + str(msg[0]) + ' Message : ' + str(msg[1])
	sys.exit()

try:
	msg = 'Sample push message'
	_SOCKET.sendto(msg,(SERVER_HOST, SERVER_PORT))
	SERVER_REPLY = _SOCKET.recvfrom(1024)

	if SERVER_REPLY:
		print str(SERVER_REPLY)
		
except socket.error, msg:
	print 'Error : ' + str(msg[0]) + ' Message : ' + str(msg[1])
	sys.exit()
 
