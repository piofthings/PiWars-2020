import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

rl = 12
fr = 13
rr = 14
fl = 15

min = 0

max = 90


kit.servo[rl].angle = min
kit.servo[fr].angle = min
kit.servo[rr].angle = min
kit.servo[fl].angle = min

time.sleep(2)
#kit.servo[rl].angle = max
#kit.servo[fr].angle = max
#kit.servo[rr].angle = max
#kit.servo[fl].angle = max
#time.sleep(2)

kit.servo[rl].angle = min
kit.servo[fr].angle = min
kit.servo[rr].angle = min
kit.servo[fl].angle = min
