# truckloads.py assigns packages to truckloads based on certain package criteria
# Author: Matthew Shelbourn | mshelbo@wgu.edu | December, 2020

from package_table import get_package_table
from distances import calc_distance


# Initially loads all trucks with packages based on truck capacity and package criteria
# These truck loads will be optimized by other functions
# 3 truck loads will be required since there are 40 packages, 2 trucks, and each
# truck has a maximum capacity of 16 packages
# O(N)
def get_truck_loads():
    packages = get_package_table()
    truck_1 = []  # first truck load to leave hub on truck #1
    truck_2 = []  # second truck load to leave hub on truck #2
    truck_3 = []  # third truck load to leave hub on either truck #1 or #2 (whichever returns first)
    linked_packages = ['13', '15', '19']
    truck_1_zips = []
    truck_2_zips = []
    truck_capacity = 16
    truck_1_count = 0
    truck_2_count = 0

    # First pass:
    # assigns packages to truck loads that must be included in specific truck loads
    # O(N)
    for el in range(1, 41):
        pkg = packages.read(el)
        if 'Delayed' in pkg[7] or 'Can' in pkg[7]:  # assigning packages to truck_2
            truck_2.append(pkg)
            truck_2_zips.append(pkg[4])
            truck_2_count += 1
            pkg[12] = True
            packages.update(el, pkg)
        elif 'Wrong' in pkg[7]:  # correcting address for package #9 & assigning it to truck_3
            pkg[1] = '410 S State St.'
            pkg[4] = '84111'
            truck_3.append(pkg)
            pkg[12] = True
            packages.update(el, pkg)
        elif 'Must' in pkg[7] or pkg[5] != 'EOD':  # assigning packages to truck_1
            truck_1.append(pkg)
            truck_1_zips.append(pkg[4])
            truck_1_count += 1
            pkg[12] = True
            packages.update(el, pkg)

    # Second pass:
    # assigns packages to truck_1 that must be delivered together
    # O(N)
    for el in range(1, 41):
        pkg = packages.read(el)
        if pkg is not None and pkg[0] in linked_packages and pkg not in truck_1:
            truck_1.append(pkg)
            truck_1_zips.append(pkg[4])
            truck_1_count += 1
            pkg[12] = True
            packages.update(el, pkg)

    # Third pass:
    # assigns packages to truck_1 while it has remaining space (based on zip code)
    # assigns packages to truck_2 while it has remaining space (based on zip code)
    # assigns all remaining packages that won't fit on truck_2 to truck_3
    # O(N)
    for el in range(1, 41):
        pkg = packages.read(el)
        if pkg[12] == False:
            if pkg is not None and truck_1_count < truck_capacity and pkg[4] in truck_1_zips:
                truck_1.append(pkg)
                truck_1_count += 1
                pkg[12] = True
                packages.update(el, pkg)
            elif pkg is not None and truck_1_count < 16:
                truck_1.append(pkg)
                truck_1_count += 1
                pkg[12] = True
                packages.update(el, pkg)
            elif pkg is not None and truck_1_count == truck_capacity and truck_2_count < truck_capacity and pkg[4] \
                    in truck_2_zips:
                truck_2.append(pkg)
                truck_2_count += 1
                pkg[12] = True
                packages.update(el, pkg)
            elif pkg is not None and truck_1_count == truck_capacity and truck_2_count < truck_capacity:
                truck_2.append(pkg)
                truck_2_count += 1
                pkg[12] = True
                packages.update(el, pkg)
            elif pkg is not None and truck_1_count == truck_capacity and truck_2_count == truck_capacity:
                truck_3.append(pkg)
                pkg[12] = True
                packages.update(el, pkg)
    return truck_1, truck_2, truck_3


# Getter for the packages on truck 1
# Optimizes the packages on truck 1 based on a nearest neighbor greedy algorithm
# O(N^2)
def get_truck_1():
    truck_1 = get_truck_loads()[0]
    truck_1_optimized = []
    previous_package = ''
    shortest_distance = 15
    truck_1_optimized_current_index = 0
    for pkg in truck_1:
        if '9' in pkg[5]:
            truck_1_optimized.append(pkg)
            truck_1.remove(pkg)
            previous_package = pkg
            truck_1_optimized_current_index += 1

    while len(truck_1) != 0:
        for pkg in truck_1:
            if float(calc_distance(previous_package, pkg)) < shortest_distance:
                try:
                    truck_1_optimized.remove(truck_1_optimized[truck_1_optimized_current_index])
                except IndexError:
                    pass
                truck_1_optimized.insert(truck_1_optimized_current_index, pkg)
                shortest_distance = float(calc_distance(previous_package, pkg))

        previous_package = truck_1_optimized[truck_1_optimized_current_index]
        truck_1.remove(previous_package)
        truck_1_optimized_current_index += 1
        shortest_distance = 15

    return truck_1_optimized


# Getter for the packages on truck 2
# Optimizes the packages on truck 2 based on a nearest neighbor greedy algorithm
# O(N^2)
def get_truck_2():
    truck_2 = get_truck_loads()[1]
    truck_2_pre_sort = []
    for pkg in truck_2:
        if 'EOD' not in pkg[5]:
            truck_2_pre_sort.insert(0, pkg)
        else:
            truck_2_pre_sort.append(pkg)

    truck_2_optimized = []
    previous_package = truck_2_pre_sort[0]
    shortest_distance = 15
    truck_2_optimized_current_index = 0

    while len(truck_2_pre_sort) != 0:
        for pkg in truck_2_pre_sort:
            if float(calc_distance(previous_package, pkg)) < shortest_distance:
                try:
                    truck_2_optimized.remove(truck_2_optimized[truck_2_optimized_current_index])
                except IndexError:
                    pass
                truck_2_optimized.insert(truck_2_optimized_current_index, pkg)
                shortest_distance = float(calc_distance(previous_package, pkg))

        previous_package = truck_2_optimized[truck_2_optimized_current_index]
        truck_2_pre_sort.remove(previous_package)
        truck_2_optimized_current_index += 1
        shortest_distance = 15

    return truck_2_optimized


# Getter for the packages on truck 3
# Optimizes the packages on truck 3 based on a nearest neighbor greedy algorithm
# O(N^2)
def get_truck_3():
    truck_3 = get_truck_loads()[2]
    truck_3_optimized = []
    previous_package = 0
    shortest_distance = 15
    truck_3_optimized_current_index = 0

    while len(truck_3) != 0:
        for pkg in truck_3:
            if float(calc_distance(previous_package, pkg)) < shortest_distance:
                try:
                    truck_3_optimized.remove(truck_3_optimized[truck_3_optimized_current_index])
                except IndexError:
                    pass
                truck_3_optimized.insert(truck_3_optimized_current_index, pkg)
                shortest_distance = float(calc_distance(previous_package, pkg))

        previous_package = truck_3_optimized[truck_3_optimized_current_index]
        truck_3.remove(previous_package)
        truck_3_optimized_current_index += 1
        shortest_distance = 15

    return truck_3_optimized

