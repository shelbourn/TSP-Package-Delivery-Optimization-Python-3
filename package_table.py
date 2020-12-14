# package_table.py ingests the data from the 'WGUPS Package File' csv and
# enters data for each package into package hash table
# Author: Matthew Shelbourn | mshelbo@wgu.edu | December, 2020

import csv
from hash_table import HashTable

# Ingest package data from 'WGUPS Package File.csv'
with open('./data/wguups-package-data.csv') as csvfile:
    package_csv = csv.reader(csvfile, delimiter=',')

    package_table = HashTable()  # Creates an instance of the hash table for packages to be entered into

    # Ingest package data from csv file and insert them into hash table as key/value pairs
    # Key == package ID / Value == array containing package details
    # O(N)
    for row in package_csv:
        package_id = row[0]
        street = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        deadline = row[5]
        weight = row[6]
        notes = row[7]
        delivery_start = ''
        current_location = ''
        delivery_time = ''
        status = ''

        package_key = int(package_id)
        package_value = [package_id, street, city, state, zip, deadline, weight, notes, delivery_start,
                         current_location, delivery_time, status]

        # Adds each key/value pair to the package hash table
        # O(N) -- Since some rows in the table may contain nested lists that need to be iterated through, the space-time
        # complexity for this operation is O(N), otherwise it would be O(1)
        package_table.create_entry(package_key, package_value)


    # Function for retrieving the full package hash table
    def get_package_table():
        return package_table
