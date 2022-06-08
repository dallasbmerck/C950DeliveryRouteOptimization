import csv
from hash_table import HashMap

# Reads the provided CSV file.
with open('input_data.csv') as csv_file_one:
    read_csv = csv.reader(csv_file_one, delimiter=',')

    hash_map = HashMap()  # Creates an instance object of ChainingHashTable class.
    first_delivery = []  # List assigned to truck 1.
    second_delivery = []  # List assigned to truck 2.
    third_delivery = []  # List assigned to truck 3.

    # Adding row values from CSV file into the chaining hash table as key:value pairs.
    # O(n)
    for row in read_csv:
        package_id = row[0]
        package_address = row[1]
        package_city = row[2]
        package_state = row[3]
        package_zip = row[4]
        package_deadline = row[5]
        package_mass = row[6]
        package_special_instructions = row[7]
        delivery_start = ''
        address_location = ''
        delivery_status = 'At hub'

        iterate_values = [package_id, address_location, package_address, package_city, package_state,
                          package_zip, package_deadline, package_mass, package_special_instructions,
                          delivery_start, delivery_status]

        # Conditional statements regarding special instructions and address changes.
        if '84104' in iterate_values[5] and '10:30' not in iterate_values[6]:
            third_delivery.append(iterate_values)
        if iterate_values[6] != 'EOD':
            if 'Must' in iterate_values[8] or 'None' in iterate_values[8]:
                first_delivery.append(iterate_values)
        if 'Can only be' in iterate_values[8] or 'Delayed' in iterate_values[8]:
            second_delivery.append(iterate_values)
        if iterate_values not in first_delivery and iterate_values not in second_delivery and iterate_values not in third_delivery:
            second_delivery.append(iterate_values) if len(second_delivery) < len(
                third_delivery) else third_delivery.append(iterate_values)

        hash_map.insert(package_id, iterate_values)

    # Packages that are assigned to the first delivery round.
    # O(1)
    def get_first_delivery():
        return first_delivery

    # Packages that are assigned to the second delivery round.
    # O(1)
    def get_second_delivery():
        return second_delivery

    # Packages that are assigned to the third delivery round.
    # O(1)
    def get_third_delivery():
        return third_delivery

    # Returns all packages from the hash table no matter their parameters.
    # O(1)
    def get_hash_table():
        return hash_map

