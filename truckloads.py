# truckloads.py assigns packages to truckloads based on certain package criteria
# Author: Matthew Shelbourn | mshelbo@wgu.edu | December, 2020

from package_table import get_package_table

# 3 truck loads will be required since there are 40 packages, 2 trucks, and each
# truck has a maximum capacity of 16 packages
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

truck_1_sorted = []
truck_2_sorted = []
truck_3_sorted = []

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
        print('Found!')
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
        elif pkg is not None and truck_1_count == truck_capacity and truck_2_count < truck_capacity and pkg[4] in truck_2_zips:
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


# Helper method to prioritize trucks based on package zip codes
# O(1)
def package_sort(pkg):
    return pkg[4]


# !!! MAKE SURE TO PRIORITIZE ALL PACKAGES WITH DEADLINES ON TRUCKS
# !!! ADJUST PACKAGE ADD FUNCTIONS TO NOT DELETE THE PACKAGE AFTER IT IS ADDED

# Getter for truck_1
def get_truck_1():
    truck_1.sort(key=package_sort)
    print(truck_1)
    return truck_1


# Getter for truck_2
def get_truck_2():
    truck_2.sort(key=package_sort)
    print(truck_2)
    return truck_2


# Getter for truck_3
def get_truck_3():
    truck_3.sort(key=package_sort)
    print(truck_3)
    return truck_3
