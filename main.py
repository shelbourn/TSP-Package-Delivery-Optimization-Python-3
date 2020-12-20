# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import datetime
from truckloads import get_truck_1, get_truck_2, get_truck_3
from package_table import get_package_table
from distances import calc_distance, get_dest_name
from durations import calc_dest_transit_time, calc_delivery_time
from routes import exec_truck_1_route

packages = get_package_table()
for el in range(1, 41):
    pkg = packages.read(el)
    print(pkg)

truck_1 = get_truck_1()
truck_2 = get_truck_2()
truck_3 = get_truck_3()

print(len(truck_1))
print(len(truck_2))
print(len(truck_3))

print(truck_1)

start_time = datetime(year=2020, month=12, day=25, hour=12, minute=0)

dist_1 = calc_distance(truck_1[0], truck_1[2])
print(dist_1)

time_1 = calc_dest_transit_time(dist_1)
calc_delivery_time(start_time, time_1)

exec_truck_1_route()

for el in range(1, 41):
    pkg = packages.read(el)
    print(pkg)