import socket
import os
from threading import Thread
from threading import Timer
import RPi.GPIO as GPIO

COMMANDS = ['on','off']
MAX_LENGTH = 4096
HEATING_TIME = 5.0

HEATER_GPIO_PIN = 13
HEATER_ON = False
HEATER_OFF = True

PORT = 31337
HOST = '127.0.0.1'

timer = None

def heaterStart():
  global timer
  print 'heaterStart()'

  if timer:
    print 'Clearing old timer'
    timer.cancel()

  print 'Turn on heater'
  GPIO.output(HEATER_GPIO_PIN, HEATER_ON)

  print 'Creating new timer with duration: '+str(HEATING_TIME)
  timer = Timer(HEATING_TIME, heaterShutdown)
  timer.start()

def heaterShutdown():
  global timer
  print 'heaterShutdown()'

  if timer:
    print 'Clearing timer'
    timer.cancel()

  print 'Shut down heater'
  GPIO.output(HEATER_GPIO_PIN, HEATER_OFF)


def handleMessage(clientsocket):
  while 1:
    buffer = clientsocket.recv(MAX_LENGTH)
    if buffer == '':
      return
    print 'Command received: '+buffer

    if not buffer in COMMANDS:
      print 'Received incorrect command!'
      return

    if buffer == 'on':
      heaterStart()

    elif buffer == 'off':
      heaterShutdown()

#Creating a socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((HOST, PORT))
serversocket.listen(10)

#Setup GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(HEATER_GPIO_PIN, GPIO.OUT)
GPIO.output(HEATER_GPIO_PIN, HEATER_OFF)

print 'Started Heater daemon (PID ' + str(os.getpid()) + ')'

while 1:
  #accept connections from outside
  (clientsocket, address) = serversocket.accept()

  ct = Thread(target=handleMessage, args=(clientsocket,))
  ct.run()
