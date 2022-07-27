# SPDX-FileCopyrightText: Copyright (c) 2022 ladyada for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense

import RPi.GPIO as GPIO
import board
import adafruit_tsc2007


ledPin = 23 # Broadcom pin 23 (P1 pin 16)

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(ledPin, GPIO.OUT) # LED pin set as output

# Initial state for LEDs:
GPIO.output(ledPin, GPIO.LOW)
# Use for I2C
i2c = board.I2C()

irq_dio = None  # don't use an irq pin by default
# uncomment for optional irq input pin so we don't continuously poll the I2C for touches
# irq_dio = digitalio.DigitalInOut(board.A0)
tsc = adafruit_tsc2007.TSC2007(i2c, irq=irq_dio)
try:
    GPIO.output(ledPin, GPIO.HIGH)
    while True:
        if tsc.touched:
            point = tsc.touch
            print("Touchpoint: (%d, %d, %d)" % (point["x"], point["y"], point["pressure"]))
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO