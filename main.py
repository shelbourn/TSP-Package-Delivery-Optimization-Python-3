# main.py contains the main logic for the progrom and the code for the console interface
# Author: Matthew Shelbourn | mshelbo@wgu.edu | December, 2020

from routes import get_total_mileage_truck_1, get_total_mileage_truck_2, get_total_mileage_truck_3,\
    get_total_transit_time_truck_2, get_total_transit_time_truck_1, get_total_transit_time_truck_3,\
    get_total_transit_time, get_total_mileage, get_truck_departure_arrival_times
from package_statuses import get_package_statuses, get_package_status

# *** TOTAL APPLICATION SPACE AND TIME COMPLEXITY IS O(N^2) ***


# Code for user interface
# O(N)
def main():
    try:
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
        main_menu = r"""
Please make a selection below by typing in the menu option on your keyboard.

1: View total transit time for all trucks to complete their routes (time while driving, not elapsed time)
2: View total mileage driven for all trucks to complete their routes
3: View the arrival and departure times for each truck to and from the hub
4: View total transit time for an individual truck (time while driving, not elapsed time)
5: View total mileage driven for an individual truck
6: View the package status for all packages based on a specific time (you will provide a time)
7: View the package status for an individual package based on a specific time (you will provide a time)
9: Return to the main menu
0: Exit the program
"""

        print(main_menu)
        user_selection = int(input('Select a menu option:\n'))

        # While loop to handle menu selection. Runs until user selects '0' to exit program
        # O(N)
        while user_selection != 0:
            if user_selection == 9:
                print(main_menu)
                user_selection = int(input('Please make another selection or type 0 to exit the program:\n'))
            elif user_selection == 1:
                print('\nThe total transit time for all trucks was ' + get_total_transit_time()[0] +
                      ' Hours and ' + get_total_transit_time()[1] + ' Minutes\n')
                user_selection = int(input('Please make another selection or type 0 to exit the program.\nTo view the '
                                           'main menu type 9:\n'))
            elif user_selection == 2:
                print('\nThe total mileage for all trucks was ' + get_total_mileage() + ' miles.\n')
                user_selection = int(input('Please make another selection or type 0 to exit the program.\nTo view the '
                                           'main menu type 9:\n'))
            elif user_selection == 3:
                print('\nDeparture and arrival times for all trucks:\n')
                get_truck_departure_arrival_times()
                user_selection = int(input('\nPlease make another selection or type 0 to exit the program.\nTo view the '
                                           'main menu type 9:\n'))
            elif user_selection == 4:
                truck_selection = int(input('\nTo see the total transit time for a specific truck please type 1 for Truck '
                                            '1, 2 for Truck 2, or 3 for Truck 3.\nType 9 to return to the main menu:\n'))
                if truck_selection == 1:
                    print('\nThe total transit time for truck ' + str(truck_selection) +
                          ' was ' + get_total_transit_time_truck_1()[0] + ' hours and ' +
                          get_total_transit_time_truck_1()[1] + ' minutes.')
                elif truck_selection == 2:
                    print('\nThe total transit time for truck ' + str(truck_selection) +
                          ' was ' + get_total_transit_time_truck_2()[0] + ' hours and ' +
                          get_total_transit_time_truck_2()[1] + ' minutes.')
                elif truck_selection == 3:
                    print('\nThe total transit time for truck ' + str(truck_selection) +
                          ' was ' + get_total_transit_time_truck_3()[0] + ' hours and ' +
                          get_total_transit_time_truck_3()[1] + ' minutes.')
                elif truck_selection == 9:
                    print(main_menu)
                    user_selection = int(input('Please make another selection or type 0 to exit the program:\n'))
            elif user_selection == 5:
                truck_selection = int(input('\nTo see the total mileage for a specific truck please type 1 for Truck '
                                            '1, 2 for Truck 2, or 3 for Truck 3.\nType 9 to return to the main menu:\n'))
                if truck_selection == 1:
                    print('\nThe total mileage driven for truck ' + str(truck_selection) +
                          ' was ' + get_total_mileage_truck_1() + ' miles.')
                elif truck_selection == 2:
                    print('\nThe total mileage driven for truck ' + str(truck_selection) +
                          ' was ' + get_total_mileage_truck_2() + ' miles.')
                elif truck_selection == 3:
                    print('\nThe total mileage driven for truck ' + str(truck_selection) +
                          ' was ' + get_total_mileage_truck_3() + ' miles.')
                elif truck_selection == 9:
                    print(main_menu)
                    user_selection = int(input('Please make another selection or type 0 to exit the program:\n'))
            elif user_selection == 6:
                time_param = input('\nPlease enter a time in 24-hour format (e.g. 14:00 for 2:00 pm, or 8 for 8:00 '
                                   'am):\n')
                if len(time_param) < 4:
                    time_param += ':00'
                print('\nStatus for all packages as of ' + time_param + ':\n')
                print(get_package_statuses(time_param))
                user_selection = int(input('Please make another selection or type 0 to exit the program.\nTo view the '
                                           'main menu type 9:\n'))
            elif user_selection == 7:
                time_param = input('\nPlease enter a time in 24-hour format (e.g. 14:00 for 2:00 pm, or 8 for 8:00 '
                                   'am):\n')
                if len(time_param) < 4:
                    time_param += ':00'
                package_selection = int(input('\nPlease type a package ID from 1-40 (e.g. 1 or 39):\n'))
                if package_selection > 40:
                    package_selection = int(input('\nInvalid Selection!\n'
                                                  'Please type a package ID from 1-40 (e.g. 1 or 39):\n'))
                print(get_package_status(package_selection, time_param))
                user_selection = int(input('Please make another selection or type 0 to exit the program.\nTo view the '
                                           'main menu type 9:\n'))
            else:
                user_selection = input('\nInvalid selection!\nPlease select a valid menu option or type 0 to exit the '
                                       'program.\nTo view the main menu type 9:\n')

    # Display message on program termination
    finally:
        print('\nThank for using the WGUPS Delivery Manager! Have a great day!\n')
        print('Goodbye!')
        return


if __name__ == '__main__':
    main()