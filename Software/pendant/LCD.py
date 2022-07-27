# External module imports
import RPi.GPIO as GPIO
# Pin Definitons:

ledPin = 23 # Broadcom pin 23 (P1 pin 16)

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(ledPin, GPIO.OUT) # LED pin set as output

# Initial state for LEDs:
GPIO.output(ledPin, GPIO.LOW)

print("Turning LCD ON")
GPIO.output(ledPin, GPIO.HIGH)
