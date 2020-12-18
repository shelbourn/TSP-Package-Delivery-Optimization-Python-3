# ingests data from "WGUPS Distance Table.csv", assigns them to objects for use in program
# Author: Matthew Shelbourn | mshelbo@wgu.edu | December, 2020

import csv

# Ingest distance data from 'wgups-distance-data.csv' and assign to list
with open('./data/wgups-distance-data.csv') as csvfile:
    distance_csv = csv.reader(csvfile, delimiter=',')
    distances = [row for row in distance_csv]

# Ingest distance address data from 'wgups-distance-addresses.csv' and assign to object
with open('./data/wgups-distance-addresses-data.csv') as csvfile:
    distance_addresses_csv = csv.reader(csvfile, delimiter=',')
    distance_addresses = {int(rows[0]): {'name': rows[1], 'address': rows[2]} for rows in distance_addresses_csv}


# Getter for distances
def get_distances():
    return distances


# Getter for addresses
def get_addresses():
    return distance_addresses
