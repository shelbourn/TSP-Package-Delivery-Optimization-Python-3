# main.py contains the main logic for the progrom and the code for the console interface
# Author: Matthew Shelbourn | mshelbo@wgu.edu | December, 2020

# !!! REMOVE UNNECESSARY PRINT STATEMENTS THROUGHOUT PROGRAM !!!

# !!! For dispatching truck 3 once truck 1 returns to the hub...
# Set the initial current time of truck 3 to the arrival time of truck 1 back to the hub

from datetime import datetime
from truckloads import get_truck_1, get_truck_2, get_truck_3
from package_table import get_package_table
from distances import calc_distance, get_dest_name
from durations import calc_dest_transit_time, calc_delivery_time
from routes import exec_truck_routes, get_total_mileage_truck_1, get_total_transit_time_truck_2
from package_statuses import get_package_statuses, get_package_status

get_package_status(2, '11:00')