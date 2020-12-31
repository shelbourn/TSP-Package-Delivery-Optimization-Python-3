# durations.py includes various operations for calculating duration and manipulating datetime objects
# Author: Matthew Shelbourn | mshelbo@wgu.edu | December, 2020

from datetime import timedelta


# Calculates transit time in minutes based on the distance parameter
# Space-time complexity O(1)
def calc_dest_transit_time(distance):
    truck_speed = 18
    transit_hours = float(distance) / truck_speed
    transit_minutes = float(transit_hours * 60)
    return transit_minutes


# Calculates the delivery time of a package based on the current_time and
# transit_minutes parameters
# Space-time complexity O(1)
def calc_delivery_time(current_time, transit_minutes):
    delivery_time = current_time + timedelta(minutes=transit_minutes)
    return delivery_time
