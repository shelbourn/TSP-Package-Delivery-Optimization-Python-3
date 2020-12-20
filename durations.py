# durations.py includes various operations for calculating duration and manipulating datetime objects
# Author: Matthew Shelbourn | mshelbo@wgu.edu | December, 2020

from datetime import timedelta


# Calculates transit time in minutes based on the distance parameter
def calc_dest_transit_time(distance):
    truck_speed = 18
    transit_hours = float(distance) / truck_speed
    transit_minutes = float(transit_hours * 60)
    print(transit_minutes)
    return transit_minutes


# Calculates the delivery time of a package based on the current_time and
# transit_minutes parameters
def calc_delivery_time(current_time, transit_minutes):
    delivery_time = current_time + timedelta(minutes=transit_minutes)
    print(delivery_time)
    return delivery_time
