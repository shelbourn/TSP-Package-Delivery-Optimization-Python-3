# package_statuses.py includes a function to calculate and return the status for all packages
# based on a given time parameter
# Author: Matthew Shelbourn | mshelbo@wgu.edu | December, 2020

from datetime import datetime, timedelta
from durations import calc_dest_transit_time, calc_delivery_time
from truckloads import get_truck_1, get_truck_2, get_truck_3
from distances import calc_distance, get_dest_name
from package_table import get_package_table


def get_package_statuses(time_param):
    packages = get_package_table()
    truck_1 = get_truck_1()
    truck_2 = get_truck_2()
    truck_3 = get_truck_3()
    current_time_truck_1 = datetime(year=2020, month=12, day=25, hour=8, minute=0)  # Tracks current time for truck 1
    current_time_truck_2 = datetime(year=2020, month=12, day=25, hour=9, minute=5)  # Tracks current time for truck 2
    current_time_truck_3 = datetime(year=2020, month=12, day=25, hour=10, minute=20)  # Tracks current time for truck 3
    current_location_truck_1 = 0  # Current location of package (initializes to 0 which refers to the index of hub)
    current_location_name_truck_1 = 'Western Governors University'  # Current name of location where package resides
    current_location_truck_2 = 0  # Current location of package (initializes to 0 which refers to the index of hub)
    current_location_name_truck_2 = 'Western Governors University'  # Current name of location where package resides
    current_location_truck_3 = 0  # Current location of package (initializes to 0 which refers to the index of hub)
    current_location_name_truck_3 = 'Western Governors University'  # Current name of location where package resides
    final_destination = 0  # Index of hub (for returning trucks to hub)
    dest_distance = 0  # Distance between each destination on route
    dest_transit_time = 0  # Transit time between each destination on route
    delivery_time = ''  # Time package was delivered
    time_param = datetime.strptime(time_param, '%H:%M')
    converted_time_param = datetime(year=2020, month=12, day=25, hour=time_param.hour, minute=time_param.minute)
    truck_1_hub_arrival_time = ''  # Needed for dispatching truck 3. Driver must return to hub before truck 3 can depart

    # Sets the initial status of all packages to 'Out for Delivery'
    # O(N)
    for pkg in truck_1:
        if current_time_truck_1 > converted_time_param + timedelta(seconds=1):
            pkg[8] = 'N/A'
            pkg[10] = 'N/A'
            packages.update(int(pkg[0]), pkg)
            continue
        else:
            pkg[8] = str(current_time_truck_1)
            pkg[10] = 'N/A'
            pkg[11] = 'Out for Delivery'
            packages.update(int(pkg[0]), pkg)

    # Delivers the packages, updates package status and delivery time
    # O(N)
    for pkg in truck_1:
        dest_distance = calc_distance(current_location_truck_1, pkg)
        dest_transit_time = calc_dest_transit_time(dest_distance)
        delivery_time = str(calc_delivery_time(current_time_truck_1, dest_transit_time))
        current_time_truck_1 = calc_delivery_time(current_time_truck_1, dest_transit_time)
        if current_time_truck_1 >= converted_time_param:
            pkg[9] = current_location_name_truck_1
            continue
        else:
            current_location_truck_1 = pkg
            current_location_name_truck_1 = get_dest_name(pkg)
            pkg[9] = current_location_name_truck_1
            pkg[10] = delivery_time
            pkg[11] = 'Delivered'
            packages.update(int(pkg[0]), pkg)

    # Returns truck 1 to the hub
    dest_distance = calc_distance(current_location_truck_1, final_destination)
    dest_transit_time = calc_dest_transit_time(dest_distance)
    current_location_name_truck_1 = get_dest_name(final_destination)
    truck_1_hub_arrival_time = calc_delivery_time(current_time_truck_1, dest_transit_time)

    # Sets the initial status of all packages to 'Out for Delivery'
    # O(N)
    for pkg in truck_2:
        if current_time_truck_2 > converted_time_param + timedelta(seconds=1):
            pkg[8] = 'N/A'
            pkg[10] = 'N/A'
            packages.update(int(pkg[0]), pkg)
            continue
        else:
            pkg[8] = str(current_time_truck_2)
            pkg[10] = 'N/A'
            pkg[11] = 'Out for Delivery'
            packages.update(int(pkg[0]), pkg)

    # Delivers the packages, updates package status and delivery time
    # O(N)
    for pkg in truck_2:
        dest_distance = calc_distance(current_location_truck_2, pkg)
        dest_transit_time = calc_dest_transit_time(dest_distance)
        delivery_time = str(calc_delivery_time(current_time_truck_2, dest_transit_time))
        current_time_truck_2 = calc_delivery_time(current_time_truck_2, dest_transit_time)
        if current_time_truck_2 >= converted_time_param:
            pkg[9] = current_location_name_truck_2
            continue
        else:
            current_location_truck_2 = pkg
            current_location_name_truck_2 = get_dest_name(pkg)
            pkg[9] = current_location_name_truck_2
            pkg[10] = delivery_time
            pkg[11] = 'Delivered'
            packages.update(int(pkg[0]), pkg)

    # DON'T KNOW IF I NEED TO RETURN TRUCK 2 TO THE HUB
    # Returns truck 2 to the hub
    # dest_distance = calc_distance(current_location_truck_2, final_destination)
    # dest_transit_time = calc_dest_transit_time(dest_distance)
    # current_location_name_truck_2 = get_dest_name(final_destination)
    # total_transit_time += int(dest_transit_time)
    # total_mileage += float(dest_distance)

    # Sets initial departure time of truck 3 based on the time that truck 1 returns to the hub
    current_time_truck_3 = current_time_truck_3 if current_time_truck_3 > truck_1_hub_arrival_time else truck_1_hub_arrival_time

    # Sets the initial status of all packages to 'Out for Delivery'
    # O(N)
    for pkg in truck_3:
        if current_time_truck_3 > converted_time_param + timedelta(seconds=1):
            pkg[8] = 'N/A'
            pkg[10] = 'N/A'
            packages.update(int(pkg[0]), pkg)
            continue
        else:
            pkg[8] = str(current_time_truck_3)
            pkg[10] = 'N/A'
            pkg[11] = 'Out for Delivery'
            packages.update(int(pkg[0]), pkg)

    # Delivers the packages, updates package status and delivery time
    # O(N)
    for pkg in truck_3:
        dest_distance = calc_distance(current_location_truck_3, pkg)
        dest_transit_time = calc_dest_transit_time(dest_distance)
        delivery_time = str(calc_delivery_time(current_time_truck_3, dest_transit_time))
        current_time_truck_3 = calc_delivery_time(current_time_truck_3, dest_transit_time)
        if current_time_truck_3 >= converted_time_param:
            pkg[9] = current_location_name_truck_3
            continue
        else:
            current_location_truck_3 = pkg
            current_location_name_truck_3 = get_dest_name(pkg)
            pkg[9] = current_location_name_truck_3
            pkg[10] = delivery_time
            pkg[11] = 'Delivered'
            packages.update(int(pkg[0]), pkg)

    # DON'T KNOW IF I NEED TO RETURN TRUCK 3 TO THE HUB
    # Returns truck 3 to the hub
    # dest_distance = calc_distance(current_location_truck_3, final_destination)
    # dest_transit_time = calc_dest_transit_time(dest_distance)
    # current_location_name_truck_3 = get_dest_name(final_destination)
    # total_transit_time += int(dest_transit_time)
    # total_mileage += float(dest_distance)

    for el in range(1, 41):
        pkg = packages.read(el)
        print('Details for package: ' + pkg[0] + ' -- Status: ' + pkg[11] + ' || Left Hub At: ' + pkg[8] + ' || Current Location: ' + pkg[9] + ' || Delivery Deadline: ' + pkg[5] + ' || Delivery Time: ' + pkg[10])

    return ''


# Returns the status of a package based on the package_id and time parameters
def get_package_status(package_id, time_param):
    packages = get_package_table()
    truck_1 = get_truck_1()
    truck_2 = get_truck_2()
    truck_3 = get_truck_3()
    current_time_truck_1 = datetime(year=2020, month=12, day=25, hour=8, minute=0)  # Tracks current time for truck 1
    current_time_truck_2 = datetime(year=2020, month=12, day=25, hour=9, minute=5)  # Tracks current time for truck 2
    current_time_truck_3 = datetime(year=2020, month=12, day=25, hour=10, minute=20)  # Tracks current time for truck 3
    current_location_truck_1 = 0  # Current location of package (initializes to 0 which refers to the index of hub)
    current_location_name_truck_1 = 'Western Governors University'  # Current name of location where package resides
    current_location_truck_2 = 0  # Current location of package (initializes to 0 which refers to the index of hub)
    current_location_name_truck_2 = 'Western Governors University'  # Current name of location where package resides
    current_location_truck_3 = 0  # Current location of package (initializes to 0 which refers to the index of hub)
    current_location_name_truck_3 = 'Western Governors University'  # Current name of location where package resides
    final_destination = 0  # Index of hub (for returning trucks to hub)
    dest_distance = 0  # Distance between each destination on route
    dest_transit_time = 0  # Transit time between each destination on route
    delivery_time = ''  # Time package was delivered
    initial_time_param = time_param
    time_param = datetime.strptime(time_param, '%H:%M')
    converted_time_param = datetime(year=2020, month=12, day=25, hour=time_param.hour, minute=time_param.minute)
    truck_1_hub_arrival_time = ''  # Needed for dispatching truck 3. Driver must return to hub before truck 3 can depart

    # Sets the initial status of all packages to 'Out for Delivery'
    # O(N)
    for pkg in truck_1:
        if current_time_truck_1 > converted_time_param + timedelta(seconds=1):
            pkg[8] = 'N/A'
            pkg[10] = 'N/A'
            packages.update(int(pkg[0]), pkg)
            continue
        else:
            pkg[8] = str(current_time_truck_1)
            pkg[10] = 'N/A'
            pkg[11] = 'Out for Delivery'
            packages.update(int(pkg[0]), pkg)

    # Delivers the packages, updates package status and delivery time
    # O(N)
    for pkg in truck_1:
        dest_distance = calc_distance(current_location_truck_1, pkg)
        dest_transit_time = calc_dest_transit_time(dest_distance)
        delivery_time = str(calc_delivery_time(current_time_truck_1, dest_transit_time))
        current_time_truck_1 = calc_delivery_time(current_time_truck_1, dest_transit_time)
        if current_time_truck_1 >= converted_time_param:
            pkg[9] = current_location_name_truck_1
            continue
        else:
            current_location_truck_1 = pkg
            current_location_name_truck_1 = get_dest_name(pkg)
            pkg[9] = current_location_name_truck_1
            pkg[10] = delivery_time
            pkg[11] = 'Delivered'
            packages.update(int(pkg[0]), pkg)

    # Returns truck 1 to the hub
    dest_distance = calc_distance(current_location_truck_1, final_destination)
    dest_transit_time = calc_dest_transit_time(dest_distance)
    current_location_name_truck_1 = get_dest_name(final_destination)
    truck_1_hub_arrival_time = calc_delivery_time(current_time_truck_1, dest_transit_time)

    # Sets the initial status of all packages to 'Out for Delivery'
    # O(N)
    for pkg in truck_2:
        if current_time_truck_2 > converted_time_param + timedelta(seconds=1):
            pkg[8] = 'N/A'
            pkg[10] = 'N/A'
            packages.update(int(pkg[0]), pkg)
            continue
        else:
            pkg[8] = str(current_time_truck_2)
            pkg[10] = 'N/A'
            pkg[11] = 'Out for Delivery'
            packages.update(int(pkg[0]), pkg)

    # Delivers the packages, updates package status and delivery time
    # O(N)
    for pkg in truck_2:
        dest_distance = calc_distance(current_location_truck_2, pkg)
        dest_transit_time = calc_dest_transit_time(dest_distance)
        delivery_time = str(calc_delivery_time(current_time_truck_2, dest_transit_time))
        current_time_truck_2 = calc_delivery_time(current_time_truck_2, dest_transit_time)
        if current_time_truck_2 >= converted_time_param:
            pkg[9] = current_location_name_truck_2
            continue
        else:
            current_location_truck_2 = pkg
            current_location_name_truck_2 = get_dest_name(pkg)
            pkg[9] = current_location_name_truck_2
            pkg[10] = delivery_time
            pkg[11] = 'Delivered'
            packages.update(int(pkg[0]), pkg)

    # Sets initial departure time of truck 3 based on the time that truck 1 returns to the hub
    current_time_truck_3 = current_time_truck_3 if current_time_truck_3 > truck_1_hub_arrival_time else truck_1_hub_arrival_time

    # Sets the initial status of all packages to 'Out for Delivery'
    # O(N)
    for pkg in truck_3:
        if current_time_truck_3 > converted_time_param + timedelta(seconds=1):
            pkg[8] = 'N/A'
            pkg[10] = 'N/A'
            packages.update(int(pkg[0]), pkg)
            continue
        else:
            pkg[8] = str(current_time_truck_3)
            pkg[10] = 'N/A'
            pkg[11] = 'Out for Delivery'
            packages.update(int(pkg[0]), pkg)

    # Delivers the packages, updates package status and delivery time
    # O(N)
    for pkg in truck_3:
        dest_distance = calc_distance(current_location_truck_3, pkg)
        dest_transit_time = calc_dest_transit_time(dest_distance)
        delivery_time = str(calc_delivery_time(current_time_truck_3, dest_transit_time))
        current_time_truck_3 = calc_delivery_time(current_time_truck_3, dest_transit_time)
        if current_time_truck_3 >= converted_time_param:
            pkg[9] = current_location_name_truck_3
            continue
        else:
            current_location_truck_3 = pkg
            current_location_name_truck_3 = get_dest_name(pkg)
            pkg[9] = current_location_name_truck_3
            pkg[10] = delivery_time
            pkg[11] = 'Delivered'
            packages.update(int(pkg[0]), pkg)

    pkg = packages.read(package_id)
    print('\nDetails for package ' + pkg[0] + ' as of ' + initial_time_param + ' --  Status: ' + pkg[11] + ' || Left Hub At: ' + pkg[
        8] + ' || Current Location: ' + pkg[9] + ' || Delivery Deadline: ' + pkg[5] + ' || Delivery Time: ' + pkg[10])

    return ''
