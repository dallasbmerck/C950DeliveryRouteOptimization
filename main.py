# Dallas Merck Student ID: 001523951

from csv_reader import get_hash_table
from packages import wgups_total_distance
import datetime


# Initial display message starts when user runs program.
print('--------------------------------------------------------')
print('Western Governors University Parcel Service')
print('--------------------------------------------------------')
print(f'Delivery route was completed in a total of {wgups_total_distance():2f} miles.')
print('--------------------------------------------------------')
print('')

convert_first_time = datetime.timedelta(hours=8)
convert_second_time = datetime.timedelta(hours=8)
user_input = input('''
    Please enter the number associated with the operation you wish to execute below or type 'exit' to exit the program.
    1. Display all package information at a specified time.
    2. Display individual package information at a specified time.
    ''')

while user_input != 'exit':
    # First case if user enters 1
    # O(n)
    if user_input == '1':
        try:
            input_time = input('Enter the time you want to search. (HH:MM:SS): ')
            (h, m, s) = input_time.split(':')
            convert_user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

            # O(n^2)
            for count in range(1, 41):
                try:
                    first_time = get_hash_table().get_value(str(count))[9]
                    second_time = get_hash_table().get_value(str(count))[10]
                    (h, m, s) = first_time.split(':')
                    convert_first_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                    (h, m, s) = second_time.split(':')
                    convert_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                except ValueError:
                    pass

                # See the packages that have left WGUPS
                if convert_first_time >= convert_user_time:
                    get_hash_table().get_value(str(count))[10] = 'At WGUPS hub'
                    get_hash_table().get_value(str(count))[9] = 'Leaves WGUPS at ' + first_time

                    print(
                        f'Package ID: {get_hash_table().get_value(str(count))[0]}, '
                        f' Delivery Status: {get_hash_table().get_value(str(count))[10]}'
                    )

                # See packages that have left but not yet reached destination.
                elif convert_first_time <= convert_user_time:
                    if convert_user_time < convert_second_time:
                        get_hash_table().get_value(str(count))[10] = 'In transit to destination'
                        get_hash_table().get_value(str(count))[9] = 'Left WGUPS at ' + first_time

                        print(
                            f'Package ID: {get_hash_table().get_value(str(count))[0]}, '
                            f'Delivery Status: {get_hash_table().get_value(str(count))[10]}'
                        )

                    # See packages that have been delivered to their destination.
                    else:
                        get_hash_table().get_value(str(count))[10] = 'Delivered to destination at ' + second_time
                        get_hash_table().get_value(str(count))[9] = 'Left WGPUS at ' + first_time

                        print(
                            f'Package ID: {get_hash_table().get_value(str(count))[0]}, '
                            f' Delivery Status: {get_hash_table().get_value(str(count))[10]}'
                        )

        except IndexError:
            print(IndexError)
            exit()
        except ValueError:
            print('Please enter a valid value.')
            exit()

    # Second case if user enters 2
    # O(n)
    elif user_input == '2':
        try:
            count = input('Please enter the ID associated with the package you wish to query. ')
            first_time = get_hash_table().get_value(str(count))[9]
            second_time = get_hash_table().get_value(str(count))[10]
            input_time = input('Enter the time you want to search in military format. (HH:MM:SS): ')
            (h, m, s) = input_time.split(':')
            convert_user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            (h, m, s) = first_time.split(':')
            convert_first_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            (h, m, s) = second_time.split(':')
            convert_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

            # See packages that have left WGUPS
            if convert_first_time >= convert_user_time:
                get_hash_table().get_value(str(count))[10] = 'At WGUPS hub.'
                get_hash_table().get_value(str(count))[9] = 'Scheduled to leave facility at ' + first_time

                print(
                    f'Package ID: {get_hash_table().get_value(str(count))[0]}\n'
                    f'Street Address: {get_hash_table().get_value(str(count))[2]}\n'
                    f'Delivery Deadline: {get_hash_table().get_value(str(count))[6]}\n'
                    f'Mass in Kilograms: {get_hash_table().get_value(str(count))[7]}\n'
                    f'Truck status: {get_hash_table().get_value(str(count))[9]}\n'
                    f'Delivery Status: {get_hash_table().get_value(str(count))[10]}\n'
                )

            # See packages that have left but not yet reached destination.
            elif convert_first_time <= convert_user_time:
                if convert_user_time < convert_second_time:
                    get_hash_table().get_value(str(count))[10] = 'In transit to destination.'
                    get_hash_table().get_value(str(count))[9] = 'Left WGUPS at ' + first_time
                    print(
                        f'Package ID: {get_hash_table().get_value(str(count))[0]}\n'
                        f'Street Address: {get_hash_table().get_value(str(count))[2]}\n'
                        f'Delivery Deadline: {get_hash_table().get_value(str(count))[6]}\n'
                        f'Mass in Kilograms: {get_hash_table().get_value(str(count))[7]}\n'
                        f'Truck status: {get_hash_table().get_value(str(count))[9]}\n'
                        f'Delivery Status: {get_hash_table().get_value(str(count))[10]}\n'
                          )

                # See packages that have been delivered to their destination.
                else:
                    get_hash_table().get_value(str(count))[10] = "Package delivered at " + second_time
                    get_hash_table().get_value(str(count))[9] = 'Left WGUPS at ' + first_time
                    print(
                        f'Package ID: {get_hash_table().get_value(str(count))[0]}\n'
                        f'Street Address: {get_hash_table().get_value(str(count))[2]}\n'
                        f'Delivery Deadline: {get_hash_table().get_value(str(count))[6]}\n'
                        f'Mass in Kilograms: {get_hash_table().get_value(str(count))[7]}\n'
                        f'Truck status: {get_hash_table().get_value(str(count))[9]}\n'
                        f'Delivery Status: {get_hash_table().get_value(str(count))[10]}\n'
                          )

        except ValueError:
            print('Please enter a valid value.')
            exit()

    # Third case if user enters 'exit'
    elif user_input == 'exit':
        exit()

    # Prints 'Invalid entry!' if the user does not input '1, 2, exit'
    else:
        print('Invalid entry!')
        exit()
