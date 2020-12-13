# pkg_truck_assn.py ingests the data from the 'WGUPS Package File' csv and
# assigns each package to 1 of 3 truckloads
# Author: Matthew Shelbourn | mshelbo@wgu.edu | December, 2020

import csv
from hash_table import HashTable

# Ingest package data from 'WGUPS Package File.csv'
with open('../')