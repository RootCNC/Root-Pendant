from encoder import Encoder
import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
#GPIO.setup(18, GPIO.IN)
#GPIO.setup(27, GPIO.IN)

def valueChanged(value,dir):	
	print(value, dir)

print("Starting encoder")
#e1 = Encoder(18, 27, callback=valueChanged)
#e1 = Encoder(18, 27)
#e1 = Encoder(20, 21)
e1 = Encoder(20, 21, callback=valueChanged)





while 1:
#	value = e1.getValue()
#	print(value)
#	print(GPIO.input(18), GPIO.input(27))
	pass


