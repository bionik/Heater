import socket
import sys

COMMANDS = ['on','off']

HOST = '127.0.0.1'
PORT = 31337

if len(sys.argv) != 2:
  print 'client.py: Missing argument'
  print 'Usage: client.py [COMMAND]'
  sys.exit(0)

if not sys.argv[1] in COMMANDS:
  print 'client.py: Incorrect command'
  print 'Available commands: ' + ', '.join(COMMANDS)
  sys.exit(0)

s = socket.socket()

print 'Connecting to socket...'
s.connect((HOST, PORT))

print 'Sending command over socket...'
s.send(sys.argv[1])

print 'Command sent.'
