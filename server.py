'''
Setting up UDP server to receive incoming events | logs
'''
import socket
import sys

# connection definitions
HOST = 'localhost'
PORT = 5000

try:
	_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print 'Socket created successfully'
except socket.error, msg:
	print 'Failed to generate socket. Error : ' + str(msg[0]) + ' Message : ' + str(msg[1])
	sys.exit()

try:
	_SOCKET.bind((HOST, PORT))
	print 'Socket bound to ' + str(HOST) + ':' + str(PORT) + ' successfully'
except socket.error, msg:
	print 'Socket binding failed. Error : ' + str(msg[0]) + ' Message : ' + str(msg[1])
	sys.exit()

while 1:
	_data_packet = _SOCKET.recvfrom(1024)
	SENDER_DATA = _data_packet[0]
	(SENDER_HOST, SENDER_PORT) = _data_packet[1]

	if not SENDER_DATA:
		# drop data_packet, report
		_SOCKET.sendto('{"Invalid push. Packet dropped"}')

	# process data_packet
	print str(SENDER_DATA) + ' from ' + str(SENDER_HOST) + ':' + str(SENDER_PORT)

	# acknowledge sender
	_SOCKET.sendto('{"Packet processed"}', (SENDER_HOST, SENDER_PORT))

_SOCKET.close()