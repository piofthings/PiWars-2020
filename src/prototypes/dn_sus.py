#!/usr/bin/env python3
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

min = 0
max = 45
kit.servo[9].angle = min
kit.servo[8].angle = min
time.sleep(2)
kit.servo[9].angle = max
kit.servo[8].angle = max
