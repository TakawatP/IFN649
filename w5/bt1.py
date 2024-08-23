import serial
import time
import string

#reading and writing data from and to arduino serially.
#rfcomm0 -> this could be different
ser = serial.Serial("/dev/rfcomm0", 9600)
ser.write(str.encode('LLED_OFF'))
