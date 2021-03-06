# Author: Matthew Shelbourn | Student ID: 001059665 | mshelbo@wgu.edu | December, 2020
# distance.py ingests data from "WGUPS Distance Table.csv", assigns them to objects for use in program

import csv

# Ingest distance data from 'wgups-distance-data.csv' and assign to list
# Space-time complexity O(N)
with open('./data/wgups-distance-data.csv') as csvfile:
    distance_csv = csv.reader(csvfile, delimiter=',')
    distances = [row for row in distance_csv]

# Ingest distance address data from 'wgups-distance-addresses.csv' and assign to object
# Space-time complexity O(N)
with open('./data/wgups-distance-addresses-data.csv') as csvfile:
    distance_addresses_csv = csv.reader(csvfile, delimiter=',')
    distance_addresses = {int(rows[0]): {'name': rows[1], 'address': rows[2]} for rows in distance_addresses_csv}


# Getter for distances
# Space-time complexity O(1)
def get_distances():
    return distances


# Getter for addresses
# Space-time complexity O(1)
def get_addresses():
    return distance_addresses


# Getter for distance_calc
# Retrieves distance between 2 addresses based on their indices in the distance matrix
# Space-time complexity O(1)
def calc_distance(add_1, add_2):
    if add_1 == 0 and add_2 == 0:
        return 0
    elif add_1 == 0:
        try:
            return distances[add_1][add_2[13]]
        except IndexError:
            return distances[add_2[13]][add_1]
    elif add_2 == 0:
        try:
            return distances[add_1[13]][add_2]
        except IndexError:
            return distances[add_2][add_1[13]]
    else:
        try:
            return distances[add_1[13]][add_2[13]]
        except IndexError:
            return distances[add_2[13]][add_1[13]]


# Getter for get_dest_name
# Retrieves the name of a destination based on a given package
# Space-time complexity O(1)
def get_dest_name(package):
    if package == 0:
        return distance_addresses[0]['name']
    else:
        return distance_addresses[package[13]]['name']