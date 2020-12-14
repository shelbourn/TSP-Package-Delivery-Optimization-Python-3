# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from package_table import get_package_table

map_test = get_package_table()
map_test.read_entry(41)
map_test.delete_entry(50)