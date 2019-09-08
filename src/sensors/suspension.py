#!/usr/bin/env python3

import time
import sys
import os

from adafruit_servokit import ServoKit
from keyboard_input import KeyboardInput

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..")) + "/models/")
from servo_status import ServoStatus

class Suspension:
    __looper = True
    __keyboardInput = KeyboardInput
    __kit = None
    __frontServoPinNumber = 0
    __rearServoPinNumber = 1

    MIN_ANGLE = 0
    MAX_ANGLE = 145

    def __init__(self, servoKit, servoStatusFile=None):
        if (servoKit != None):
            self.__kit = servoKit
            self.__kit.servo[self.__frontServoPinNumber].angle = self.MIN_ANGLE
            self.__kit.servo[self.__rearServoPinNumber].angle = self.MIN_ANGLE
        if(servoStatusFile != None):
            self.servo_status = ServoStatus(json_file=servoStatusFile)
            self.__frontServoPinNumber = self.servo_status.suspension_front_port
            self.__rearServoPinNumber = self.servo_status.suspension_rear_port
            self.move_servo_to(1, self.servo_status.suspension_front_start)
            self.move_servo_to(2, self.servo_status.suspension_rear_start)

    def set_front_suspension_port(self, port):
        self.__frontServoPinNumber = int(port)

    def set_rear_suspension_port(self, port):
        self.__rearServoPinNumber = int(port)

    def move_servo_to(self, index, value):
        if(index == 1):
            self.__kit.servo[int(self.servo_status.suspension_front_port)].angle = value
        elif(index == 2):
            self.__kit.servo[int(self.servo_status.suspension_rear_port)].angle = value

    def raise_front_by(self, degrees):
        final = self.__kit.servo[self.__frontServoPinNumber].angle - degrees
        if(final > self.MAX_ANGLE):
            self.__kit.servo[self.__frontServoPinNumber].angle = final
        else:
            self.__kit.servo[self.__frontServoPinNumber].angle = self.MAX_ANGLE

    def raise_rear_by(self, degrees):
        final = self.__kit.servo[self.__frontServoPinNumber].angle - degrees
        if(final > self.MAX_ANGLE):
            self.__kit.servo[self.__rearServoPinNumber].angle = final
        else:
            self.__kit.servo[self.__rearServoPinNumber].angle = self.MAX_ANGLE

    def lower_front_by(self, degrees):
        final = self.__kit.servo[self.__frontServoPinNumber] + degrees
        if(final < self.MIN_ANGLE):
            self.__kit.servo[self.__frontServoPinNumber].angle = final
        else:
            self.__kit.servo[self.__frontServoPinNumber].angle = self.MIN_ANGLE

    def raise_both_by(self, degrees):
        final = self.__kit.servo[self.__frontServoPinNumber].angle - degrees
        if(final > self.MAX_ANGLE):
            self.__kit.servo[self.__frontServoPinNumber].angle = final
            self.__kit.servo[self.__rearServoPinNumber].angle = final
        else:
            self.__kit.servo[self.__frontServoPinNumber].angle = self.MAX_ANGLE
            self.__kit.servo[self.__rearServoPinNumber].angle = self.MAX_ANGLE

    def lower_both_by(self, degrees):
        final = self.__kit.servo[self.__frontServoPinNumber] + degrees
        if(final < self.MIN_ANGLE):
            self.__kit.servo[self.__frontServoPinNumber].angle = final
            self.__kit.servo[self.__rearServoPinNumber].angle = final
        else:
            self.__kit.servo[self.__frontServoPinNumber].angle = self.MIN_ANGLE
            self.__kit.servo[self.__rearServoPinNumber].angle = self.MIN_ANGLE
