# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import datetime
from truckloads import get_truck_1, get_truck_2, get_truck_3
from package_table import get_package_table
from distances import calc_distance, get_dest_name
from durations import calc_dest_transit_time, calc_delivery_time
from routes import exec_truck_routes, get_total_mileage_truck_1, get_total_transit_time_truck_2
from package_statuses import get_package_statuses

print(get_total_mileage_truck_1())
print(get_total_transit_time_truck_2()[1] + ' Minutes')