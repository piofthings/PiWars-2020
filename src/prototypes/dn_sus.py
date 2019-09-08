#!/usr/bin/env python3
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

min = 0
max = 145
kit.servo[0].angle = min
kit.servo[1].angle = min
time.sleep(2)
kit.servo[0].angle = max
kit.servo[1].angle = max
