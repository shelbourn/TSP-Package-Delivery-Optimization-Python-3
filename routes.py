# routes.py includes various functions for calculating & executing delivery routes
# The logic in this file will actually execute the truck delivery routes and deliver packages
# Author: Matthew Shelbourn | mshelbo@wgu.edu | December, 2020

from datetime import datetime, timedelta
import time
from durations import calc_dest_transit_time, calc_delivery_time
from truckloads import get_truck_1, get_truck_2, get_truck_3
from distances import calc_distance, get_dest_name
from package_table import get_package_table

packages = get_package_table()


# Executing delivery route for Truck 1
def exec_truck_routes():
    truck_1 = get_truck_1()
    truck_2 = get_truck_2()
    truck_3 = get_truck_3()
    current_time_truck_1 = datetime(year=2020, month=12, day=25, hour=8, minute=0)  # Tracks current time for truck 1
    current_time_truck_2 = datetime(year=2020, month=12, day=25, hour=9, minute=5)  # Tracks current time for truck 2
    current_time_truck_3 = datetime(year=2020, month=12, day=25, hour=10, minute=20)  # Tracks current time for truck 3
    current_location_truck_1 = 0  # Current location of package (initializes to 0 which refers to the index of hub)
    current_location_name_truck_1 = ''  # Current name of location where package resides
    current_location_truck_2 = 0  # Current location of package (initializes to 0 which refers to the index of hub)
    current_location_name_truck_2 = ''  # Current name of location where package resides
    current_location_truck_3 = 0  # Current location of package (initializes to 0 which refers to the index of hub)
    current_location_name_truck_3 = ''  # Current name of location where package resides
    final_destination = 0  # Index of hub (for returning trucks to hub)
    dest_distance = 0  # Distance between each destination on route
    dest_transit_time = 0  # Transit time between each destination on route
    delivery_time = ''  # Time package was delivered
    total_mileage_truck_1 = 0
    total_mileage_truck_2 = 0
    total_mileage_truck_3 = 0
    total_transit_time_truck_1 = 0
    total_transit_time_truck_2 = 0
    total_transit_time_truck_3 = 0
    total_mileage = 0
    total_transit_time = 0
    truck_1_hub_arrival_time = ''  # Needed for dispatching truck 3. Driver must return to hub before truck 3 can depart

    print('Truck 1 left hub at: ' + str(current_time_truck_1))

    # Sets the initial status of all packages to 'Out for Delivery'
    # O(N)
    for pkg in truck_1:
        pkg[8] = str(current_time_truck_1)
        pkg[9] = 'Western Governors University'
        pkg[10] = 'N/A'
        pkg[11] = 'Out for Delivery'
        packages.update(int(pkg[0]), pkg)

    # Delivers the packages, updates package status and delivery time
    # O(N)
    for pkg in truck_1:
        print(pkg)
        dest_distance = calc_distance(current_location_truck_1, pkg)
        dest_transit_time = calc_dest_transit_time(dest_distance)
        delivery_time = str(calc_delivery_time(current_time_truck_1, dest_transit_time))
        current_time_truck_1 = calc_delivery_time(current_time_truck_1, dest_transit_time)
        current_location_truck_1 = pkg
        current_location_name_truck_1 = get_dest_name(pkg)
        pkg[9] = current_location_name_truck_1
        pkg[10] = delivery_time
        pkg[11] = 'Delivered'
        packages.update(int(pkg[0]), pkg)
        total_transit_time += int(dest_transit_time)
        total_mileage += float(dest_distance)
        print(pkg)

    # Returns truck 1 to the hub
    dest_distance = calc_distance(current_location_truck_1, final_destination)
    dest_transit_time = calc_dest_transit_time(dest_distance)
    current_location_name_truck_1 = get_dest_name(final_destination)
    total_transit_time += int(dest_transit_time)
    total_transit_time_truck_1 += int(dest_transit_time)
    total_mileage += float(dest_distance)
    total_mileage_truck_1 += float(dest_distance)
    truck_1_hub_arrival_time = calc_delivery_time(current_time_truck_1, dest_transit_time)
    print('Truck 1 returned to hub at: ' + str(truck_1_hub_arrival_time))

    # Prints total transit time and total mileage
    print('Total Transit Time: ' + str(total_transit_time))
    print('Total Mileage: ' + str(total_mileage))

    print('Truck 2 left hub at: ' + str(current_time_truck_2))

    # Sets the initial status of all packages to 'Out for Delivery'
    # O(N)
    for pkg in truck_2:
        pkg[8] = str(current_time_truck_2)
        pkg[9] = 'Western Governors University'
        pkg[10] = 'N/A'
        pkg[11] = 'Out for Delivery'
        packages.update(int(pkg[0]), pkg)

    # Delivers the packages, updates package status and delivery time
    # O(N)
    for pkg in truck_2:
        print(pkg)
        dest_distance = calc_distance(current_location_truck_2, pkg)
        dest_transit_time = calc_dest_transit_time(dest_distance)
        delivery_time = str(calc_delivery_time(current_time_truck_2, dest_transit_time))
        current_time_truck_2 = calc_delivery_time(current_time_truck_2, dest_transit_time)
        current_location_truck_2 = pkg
        current_location_name_truck_2 = get_dest_name(pkg)
        pkg[9] = current_location_name_truck_2
        pkg[10] = delivery_time
        pkg[11] = 'Delivered'
        packages.update(int(pkg[0]), pkg)
        total_transit_time += int(dest_transit_time)
        total_transit_time_truck_2 += int(dest_transit_time)
        total_mileage += float(dest_distance)
        total_mileage_truck_2 += float(dest_distance)
        print(pkg)

    # DON'T KNOW IF I NEED TO RETURN TRUCK 2 TO THE HUB
    # Returns truck 2 to the hub
    # dest_distance = calc_distance(current_location_truck_2, final_destination)
    # dest_transit_time = calc_dest_transit_time(dest_distance)
    # current_location_name_truck_2 = get_dest_name(final_destination)
    # total_transit_time += int(dest_transit_time)
    # total_mileage += float(dest_distance)

    # Prints total transit time and total mileage
    print('Total Transit Time: ' + str(total_transit_time))
    print('Total Mileage: ' + str(total_mileage))

    # Sets initial departure time of truck 3 based on the time that truck 1 returns to the hub
    current_time_truck_3 = current_time_truck_3 if current_time_truck_3 > truck_1_hub_arrival_time else truck_1_hub_arrival_time

    print('Truck 3 left hub at: ' + str(current_time_truck_3))

    # Sets the initial status of all packages to 'Out for Delivery'
    # O(N)
    for pkg in truck_3:
        pkg[8] = str(current_time_truck_3)
        pkg[9] = 'Western Governors University'
        pkg[10] = 'N/A'
        pkg[11] = 'Out for Delivery'
        packages.update(int(pkg[0]), pkg)

    # Delivers the packages, updates package status and delivery time
    # O(N)

    for pkg in truck_3:
        print(pkg)
        dest_distance = calc_distance(current_location_truck_3, pkg)
        dest_transit_time = calc_dest_transit_time(dest_distance)
        delivery_time = str(calc_delivery_time(current_time_truck_3, dest_transit_time))
        current_time_truck_3 = calc_delivery_time(current_time_truck_3, dest_transit_time)
        current_location_truck_3 = pkg
        current_location_name_truck_3 = get_dest_name(pkg)
        pkg[9] = current_location_name_truck_3
        pkg[10] = delivery_time
        pkg[11] = 'Delivered'
        packages.update(int(pkg[0]), pkg)
        total_transit_time += int(dest_transit_time)
        total_transit_time_truck_3 += int(dest_transit_time)
        total_mileage += float(dest_distance)
        total_mileage_truck_3 += float(dest_distance)
        print(pkg)

    # DON'T KNOW IF I NEED TO RETURN TRUCK 3 TO THE HUB
    # Returns truck 3 to the hub
    # dest_distance = calc_distance(current_location_truck_3, final_destination)
    # dest_transit_time = calc_dest_transit_time(dest_distance)
    # current_location_name_truck_3 = get_dest_name(final_destination)
    # total_transit_time += int(dest_transit_time)
    # total_mileage += float(dest_distance)

    # Prints total transit time and total mileage
    print('Total Transit Time: ' + str(total_transit_time))
    print('Total Mileage: ' + str(total_mileage))

    # Returns total_transit_time and total_mileage
    return total_transit_time, total_transit_time_truck_1, total_transit_time_truck_2, \
           total_transit_time_truck_3, total_mileage, total_mileage_truck_1, total_mileage_truck_2, \
           total_mileage_truck_3


# Getter for total_transit_time
def get_total_transit_time():
    time_sec = exec_truck_routes()[0] * 60
    time_convert = time.gmtime(time_sec)
    hours = time.strftime('%H', time_convert)
    minutes = time.strftime('%M', time_convert)
    return hours, minutes


# Getter for total_transit_time_truck_1
def get_total_transit_time_truck_1():
    time_sec = exec_truck_routes()[1] * 60
    time_convert = time.gmtime(time_sec)
    hours = time.strftime('%H', time_convert)
    minutes = time.strftime('%M', time_convert)
    return hours, minutes


# Getter for total_transit_time_truck_2
def get_total_transit_time_truck_2():
    time_sec = exec_truck_routes()[2] * 60
    time_convert = time.gmtime(time_sec)
    hours = time.strftime('%H', time_convert)
    minutes = time.strftime('%M', time_convert)
    return hours, minutes


# Getter for total_transit_time_truck_3
def get_total_transit_time_truck_3():
    time_sec = exec_truck_routes()[3] * 60
    time_convert = time.gmtime(time_sec)
    hours = time.strftime('%H', time_convert)
    minutes = time.strftime('%M', time_convert)
    return hours, minutes


# Getter for total_mileage
def get_total_mileage():
    return str(round(exec_truck_routes()[4], 2))


# Getter for total_mileage_truck_1
def get_total_mileage_truck_1():
    return str(round(exec_truck_routes()[5], 2))


# Getter for total_mileage_truck_2
def get_total_mileage_truck_2():
    return str(round(exec_truck_routes()[6], 2))


# Getter for total_mileage_truck_3
def get_total_mileage_truck_3():
    return str(round(exec_truck_routes()[7], 2))