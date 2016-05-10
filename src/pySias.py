'''
Created on 10 mag 2016

@author: sbacchetta
'''

import serial
import sys
import socket

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

print("pySias")
#print(serial_ports())
port = 12345
address = "172.16.35.168"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((address,port))
while True:
    data = sock.recvfrom(1024) # buffer size is 1024 bytes
    print ("received message:", data)