# HashTable.py contains the Class constructors and associated methods for the HashEntry and HashTable classes
# Author: Matthew Shelbourn | mshelbo@wgu.edu | December, 2020

# Class constructor for an individual Hash Table entry

class HashEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

# Class constructor for the Hash Table to be used for all packages
# The HashTable class includes the following:
    # Methods for: defining the empty table, defining the hash key, adding an item to the table, retrieving an item from the table,
    # updating an item in the table, and deleting an item from the table

class HashTable:

    # Creates the empty hash table with empty arrays (buckets) in each row of table
    # The number of rows can be controlled by the MAX variable
    def __init__(self):
        self.MAX = 10
        self.table = [[] for i in range(self.MAX)]

    # Defines the hashing function
    def get_hash(self, key):
        return int(key) % len(self.table)

    # Function for adding a key/value pair to the hash table
    def __add_item__(self, key, val):
        hashed_key = self.get_hash(key)
        found = False

        # Determine if key already exists & update value if it does
        # If not found, then a new key/value pair is appended to the list for that hashed key
        for i, el in enumerate(self.table[hashed_key]):
            if len(el) == 2 and el[0] == key:
                self.table[hashed_key][i] = (key, val)
                found = True
                break
        if not found:
            self.table[hashed_key].append((key, val))
