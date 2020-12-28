# package_table.py ingests the data from the 'WGUPS Package File' csv and
# enters data for each package into package hash table
# Author: Matthew Shelbourn | mshelbo@wgu.edu | December, 2020

import csv
from hash_table import HashTable
from distances import get_addresses

# Getter for package_table
# O(N^2)
def get_package_table():
    # Ingest package data from 'WGUPS Package File.csv'
    with open('./data/wgups-package-data.csv') as csvfile:
        package_csv = csv.reader(csvfile, delimiter=',')

        package_table = HashTable()  # Creates an instance of the hash table for packages to be entered into
        addresses = get_addresses()  # Assigning addresses to local variable

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
            left_hub = ''
            current_location = "Western Governors University"
            delivery_time = ''
            status = 'At the Hub'
            assigned = False

            package_key = int(package_id)
            package_value = [package_id, street, city, state, zip, deadline, weight, notes, left_hub,
                             current_location, delivery_time, status, assigned]

            # Adds each key/value pair to the package hash table
            # O(N) -- Since some rows in the table may contain nested lists that need to be iterated through, the space-time
            # complexity for this operation is O(N), otherwise it would be O(1)
            package_table.create(package_key, package_value)

        # Iterates over packages and assigns a package address index based on the
        # distance_addresses variable in distances.py
        # This index will help to simplify distance calculations necessary in the program
        # O(N^2)
        for el in range(1, 41):
            pkg = package_table.read(el)
            address_index = ''
            address = pkg[1]
            for key, value in addresses.items():
                if address in value['address']:
                    address_index = key
                    pkg.append(address_index)
            package_table.update(el, pkg)

    return package_table
