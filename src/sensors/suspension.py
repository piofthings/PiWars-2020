#!/usr/bin/env python3

import time
from adafruit_servokit import ServoKit
from keyboard_input import KeyboardInput


class Suspension:
    __looper = True
    __keyboardInput = KeyboardInput
    __kit = None
    __frontServoPinNumber = 0
    __rearServoPinNumber = 1
    MIN_ANGLE = 115
    MAX_ANGLE = 0

    def __init__(self, servoKit, frontServoPinNumber, rearServoPinNumber):
        self.__frontServoPinNumber = frontServoPinNumber
        self.__rearServoPinNumber = rearServoPinNumber
        if (servoKit != None):
            self.__kit = servoKit
            self.__kit.servo[self.__frontServoPinNumber].angle = self.MIN_ANGLE
            self.__kit.servo[self.__rearServoPinNumber].angle = self.MIN_ANGLE

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
