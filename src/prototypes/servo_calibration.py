#!/usr/bin/env python3
"""

"""
import math
import time
import os.path
import sys

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..")) + "/models/")

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..")) + "/sensors/")

from servo_status import ServoStatus
from keyboard_input import KeyboardInput
from steering import Steering
from suspension import Suspension

class ServoCalibration:
    __kit = None
    __looper = True
    __keyboardInput = None
    __steering = None
    __suspension = None

    def __init__(self, servoKit):
        self.__kit = servoKit
        self.__keyboardInput = KeyboardInput("Steering Calibration")
        config_file = servoStatusFile=os.path.abspath(os.path.join(
            os.path.dirname(__file__), "..")) + "/config/servo_status.json"
        self.__steering = Steering(self.__kit, config_file)
        self.__suspension = Suspension(self.__kit, config_file)
    def menu(self):
        self.__keyboardInput.clear()
        print("J2 Controller Steering Calibration Menu:")
        print()
        print("c: Setup Wheel ports (On Adafruit PWM Board)")
        print("n: Setup Suspension ports (On Adafruit PWM Board)")
        print("w: Front left Wheel")
        print("e: Front right Wheel")
        print("s: Rear left Wheel")
        print("d: Rear right Wheel")
        print("o: Front Suspension")
        print("k: Rear Suspension")
        print("r: Save current status")
        print("t: Reset all to *_start angle in sttering_status.json")
        print("a: Set Actuation Angle")
        print("--------------------")
        print("q: Back")
        print("")
        self.waitForInput()

    def waitForInput(self):
        while self.__looper:
            keyp = self.__keyboardInput.readkey()
            if(keyp == 'q'):
                print("Saving...")
                self.__steering.save_servo_status()
                print("Quit")
                self.__looper = False
            elif(keyp == 'c'):
                print("Enter Port on which front_left steering motor is: ")
                self.__steering.set_steering_port(Steering.FRONT_LEFT_POS, input())
                print("Enter Port on which front_right steering motor is: ")
                self.__steering.set_steering_port(Steering.FRONT_RIGHT_POS, input())
                print("Enter Port on which rear_left steering motor is: ")
                self.__steering.set_steering_port(Steering.REAR_LEFT_POS, input())
                print("Enter Port on which rear_right steering motor is: ")
                self.__steering.set_steering_port(Steering.REAR_RIGHT_POS, input())
                self.__steering.save_servo_status()
            elif(keyp == 'w'):
                self.calibrate_steering(1)
            elif(keyp == 'e'):
                self.calibrate_steering(2)
            elif(keyp == 's'):
                self.calibrate_steering(3)
            elif(keyp == 'd'):
                self.calibrate_steering(4)
            elif(keyp == 'r'):
                self.__steering.save_servo_status()
                print("Saved to file", end='\r', flush=True)
            elif(keyp == 't'):
                self.__steering.move_servo_to(Steering.FRONT_LEFT_POS, self.__steering.servo_status.front_left_start)
                self.__steering.move_servo_to(Steering.FRONT_RIGHT_POS, self.__steering.servo_status.front_right_start)
                self.__steering.move_servo_to(Steering.REAR_LEFT_POS, self.__steering.servo_status.rear_left_start)
                self.__steering.move_servo_to(Steering.REAR_RIGHT_POS, self.__steering.servo_status.rear_right_start)
                print("\r\n Servos updated")
                print("\r\n Servo status")
                self.__steering.print_servo_stats()
            elif (keyp == 'a'):
                print("Set actuation degrees [180-270]: ")
                self.__steering.set_actuation_degrees(int(input()))
            time.sleep(0.01)

    def calibrate_steering(self, index):
        waitForWheel = True
        keyboardInput = KeyboardInput("Calibrate Steering:")
        print("Press Up/Down to test or w/z to adjust wheel delta, 0 to reset, q when done")
        while waitForWheel:
            key = keyboardInput.readkey()
            if(key == 'w'):
                self.__steering.increment_position(index, 1)
                self.__steering.update_servos()
            elif(ord(key) == 16):
                self.__steering.move_servo_by(index, 1)
            elif(key == 'z'):
                self.__steering.decrement_position(index, 1)
                self.__steering.update_servos()
            elif(ord(key) == 17):
                self.__steering.move_servo_by(index, -1)
            elif(key == 'q'):
                self.__steering.save_servo_status()
                waitForWheel = False
            time.sleep(0.01)
