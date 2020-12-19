# durations.py includes various operations for calculating duration and manipulating datetime objects
# Author: Matthew Shelbourn | mshelbo@wgu.edu | December, 2020

from datetime import datetime, timedelta

truck_speed = 18

def dest_transit_time(distance):
    transit_hours = distance / truck_speed
    transit_minutes = int(round(transit_hours * 60))