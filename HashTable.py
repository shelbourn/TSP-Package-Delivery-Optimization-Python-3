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
    # The hash table add_item function uses chaining for collision handling

class HashTable:

    # Creates the empty hash table with empty arrays (buckets) in each row of table
    # The number of rows can be controlled by the MAX variable
    # O(1)
    def __init__(self):
        self.MAX = 10
        self.table = [[] for i in range(self.MAX)]

    # Defines the hashing function
    # O(1)
    def get_hash(self, key):
        return int(key) % len(self.table)

    # <----- BEGIN CRUD FUNCTIONALITY ----->

    # Function for adding a key/value pair to the hash table
    # O(N)
    def __create_entry__(self, key, val):
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

    # Function for retrieving entries from the table
    # O(N)
    def __read_entry__(self, key):
        hashed_key = self.get_hash(key)
        found = False

        for el in self.table[hashed_key]:
            if el[0] == key:
                found = True
                return el[1]
        if not found:
            print("Unable to locate a package with the ID:", key)
            print("Please double check the ID and try again.")
            return None

    # Function for updating hash table entries
    # O(N)
    def __update_entry__(self, key, val):
        hashed_key = self.get_hash(key)
        found = False

        for i, el in enumerate(self.table[hashed_key]):
            if len(el) == 2 and el[0] == key:
                self.table[hashed_key][i] = (key, val)
                found = True
                break
        if not found:
            print("Unable to update the package with ID:", key)
            print("No package found with ID:", key)
            print("Please double check the ID and try again.")
            return None

    def __delete_entry__(self, key):
        hashed_key = self.get_hash(key)
        found = False



    # <----- END CRUD FUNCTIONALITY ----->
