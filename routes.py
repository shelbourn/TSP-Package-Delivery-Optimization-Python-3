# routes.py includes various functions for calculating & executing delivery routes
# The logic in this file will actually execute the truck delivery routes and deliver packages
# Author: Matthew Shelbourn | mshelbo@wgu.edu | December, 2020

from datetime import datetime
from durations import calc_dest_transit_time, calc_delivery_time
from truckloads import get_truck_1, get_truck_2, get_truck_3
from distances import calc_distance, get_dest_name
from package_table import get_package_table

packages = get_package_table()
start_time_truck_3 = datetime(year=2020, month=12, day=25, hour=9, minute=5)
start_time_truck_3 = datetime(year=2020, month=12, day=25, hour=10, minute=20)


# Executing delivery route for Truck 1
def exec_truck_1_route():
    truck_1 = get_truck_1()
    start_time_truck_1 = datetime(year=2020, month=12, day=25, hour=8, minute=0)
    current_location = 0  # Current location of package (initializes to 0 which refers to the index of hub)
    current_location_name = ''  # Current name of location where package resides
    final_destination = 0  # Index of hub (for returning truck 1 to hub)
    dest_distance = 0  # Distance between each destination on route
    dest_transit_time = 0  # Transit time between each destination on route
    delivery_time = ''  # Time package was delivered
    total_mileage = 0
    total_transit_time = 0

    # Sets the initial status of all packages to 'Out for Delivery'
    # O(N)
    for pkg in truck_1:
        pkg[11] = 'Out for Delivery'
        packages.update(int(pkg[0]), pkg)

    # Delivers the packages, updates package status and delivery time
    # O(N)
    for pkg in truck_1:
        print(pkg)
        dest_distance = calc_distance(current_location, pkg)
        dest_transit_time = calc_dest_transit_time(dest_distance)
        delivery_time = str(calc_delivery_time(start_time_truck_1, dest_transit_time))
        current_location = pkg
        current_location_name = get_dest_name(pkg)
        pkg[9] = current_location_name
        pkg[10] = delivery_time
        pkg[11] = 'Delivered'
        packages.update(int(pkg[0]), pkg)
        total_transit_time += int(dest_transit_time)
        total_mileage += float(dest_distance)
        print(pkg)

    # Returns truck 1 to the hub
    dest_distance = calc_distance(current_location, final_destination)
    dest_transit_time = calc_dest_transit_time(dest_distance)
    current_location_name = get_dest_name(final_destination)
    total_transit_time += int(dest_transit_time)
    total_mileage += float(dest_distance)

    # Prints total transit time and total mileage
    print('Total Transit Time: ' + str(total_transit_time))
    print('Total Mileage: ' + str(total_mileage))

    # Returns total_transit_time and total_mileage
    return total_transit_time, total_mileage
