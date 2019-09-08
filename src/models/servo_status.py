#!/user/bin/python3

import json
from serialisable_base import SerialisableBase


class ServoStatus(SerialisableBase):
    front_left_port = -1
    front_right_port = -1
    rear_left_port = -1
    rear_right_port = -1
    front_left_delta = 0
    front_right_delta = 0
    rear_left_delta = 0
    rear_right_delta = 0
    front_right_start = 90
    front_left_start = 90
    rear_left_start = 90
    rear_right_start = 90
    actuation_range = 160
    suspension_front_port = 0
    suspension_rear_port = 1
    suspension_front_max = 145
    suspension_front_min = 0
    suspension_rear_max = 145
    suspension_rear_min = 0
    suspension_rear_start = 0
    suspension_front_start = 0
    def __init__(self, json_def=None, json_file=None):
        super().__init__(json_def, json_file)
