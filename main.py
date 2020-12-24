# main.py contains the main logic for the progrom and the code for the console interface
# Author: Matthew Shelbourn | mshelbo@wgu.edu | December, 2020

# !!! REMOVE UNNECESSARY PRINT STATEMENTS THROUGHOUT PROGRAM !!!

# !!! For dispatching truck 3 once truck 1 returns to the hub...
# Set the initial current time of truck 3 to the arrival time of truck 1 back to the hub

from datetime import datetime
from truckloads import get_truck_1, get_truck_2, get_truck_3
from package_table import get_package_table
from distances import calc_distance, get_dest_name
from durations import calc_dest_transit_time, calc_delivery_time
from routes import exec_truck_routes, get_total_mileage_truck_1, get_total_transit_time_truck_2
from package_statuses import get_package_statuses, get_package_status

# 1: Print total transit time
# 2: Print total mileage
# 3: Print all package statuses based on a given time
# 4: Print individual package status based on a given time
# 0: Exit Application

# Code for user interface
def main():
    print('')
    print('Welcome to the WGUPS Delivery Manager!')

    # Begin art ----->
    print(r"""
  _      _________  _____  ____  ___      ___                     __  ___                           
 | | /| / / ___/ / / / _ \/ __/ / _ \___ / (_)  _____ ______ __  /  |/  /__ ____  ___ ____ ____ ____
 | |/ |/ / (_ / /_/ / ___/\ \  / // / -_) / / |/ / -_) __/ // / / /|_/ / _ `/ _ \/ _ `/ _ `/ -_) __/
 |__/|__/\___/\____/_/  /___/ /____/\__/_/_/|___/\__/_/  \_, / /_/  /_/\_,_/_//_/\_,_/\_, /\__/_/   
                                                        /___/                        /___/          """)
    print(r"""
                        _____________________________________________________
                      |                                                     |
             _______  |                                                     |
            / _____ | |                  WGU Postal Service                 |
           / /(__) || |                                                     |
  ________/ / |OO| || |                                                     |
 |         |-------|| |                                                     |
(|         |     -.|| |_______________________                              |
 |  ____   \       ||_________||____________  |             ____      ____  |
/| / __ \   |______||     / __ \   / __ \   | |            / __ \    / __ \ |\
\|| /  \ |_______________| /  \ |_| /  \ |__| |___________| /  \ |__| /  \|_|/
   | () |                 | () |   | () |                  | () |    | () |
    \__/                   \__/     \__/                    \__/      \__/
    """)

    # Begin functionality ----->
    print('Please make a selection below by typing in the menu option on your keyboard.')
    print('')

    user_selection = int(input('Select a menu option:'))
    print('1: View total transit time for all trucks to complete their routes (time while driving, not elapsed time)')
    print('2: View total mileage driven for all trucks to complete their routes')

    # While loop to handle menu selection. Runs until user selects '0' to exit program
    # O(N)
    while user_selection is not 0:


    return


if __name__ == '__main__':
    main()