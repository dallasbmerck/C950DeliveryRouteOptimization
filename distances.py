import csv
import datetime

# Read the data from the CSV files to use for routing.
with open('distance_data.csv') as csv_file_one:
    distance_CSV = list(csv.reader(csv_file_one, delimiter=','))
with open('distance_name_data.csv') as csv_file_two:
    name_CSV = list(csv.reader(csv_file_two, delimiter=','))

    # Retrieves the address associated with each package to be delivered.
    # O(1)
    def retrieve_address():
        return name_CSV

    # Retrieves the total distance values between each address from the WGUPSDistanceData.csv file.
    # O(1)
    def get_distance(row, column, total):
        distance = distance_CSV[row][column]
        if distance == '':
            distance = distance_CSV[column][row]
        return total + float(distance)

    # Retrieves the current distance values between each address from the WGUPSDistanceData.csv file.
    # O(1)
    def retrieve_current_distance(row, column):
        distance = distance_CSV[row][column]
        if distance == '':
            distance = distance_CSV[column][row]

        return float(distance)

    # Get the total distance traveled in relation to time for a given truck.
    # O(n)
    def get_truck_time(distance, trucks_list):
        new_time = distance / 18  # Average speed of trucks.
        distance_minutes = '{0:02.0f}:{1:02.0f}'.format(
            *divmod(new_time * 60, 60))
        final_time = distance_minutes + ':00'
        trucks_list.append(final_time)
        total = datetime.timedelta()
        for i in trucks_list:
            (h, m, s) = i.split(':')
            total += datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        return total


    # New lists to contain the "optimized" trucks that improve efficiency and their indices.
    first_truck = []
    first_truck_indices = []
    second_truck = []
    second_truck_indices = []
    third_truck = []
    third_truck_indices = []

    # This algorithm contains a greedy heuristic
    # Space-Time Complexity -> O(n^2)
    def find_optimal_route(distance_list, truck_number, current_location):
        if not len(distance_list):
            return distance_list

        lowest_distance_value = 999.0
        location = 0

        for i in distance_list:
            value = int(i[1])
            if retrieve_current_distance(current_location, value) <= lowest_distance_value:
                lowest_distance_value = retrieve_current_distance(current_location, value)
                location = value

        for i in distance_list:
            if retrieve_current_distance(current_location, int(i[1])) == lowest_distance_value:
                if truck_number == 1:
                    first_truck.append(i)
                    first_truck_indices.append(i[1])
                    distance_list.pop(distance_list.index(i))
                    current_location = location
                    find_optimal_route(distance_list, 1, current_location)
                elif truck_number == 2:
                    second_truck.append(i)
                    second_truck_indices.append(i[1])
                    distance_list.pop(distance_list.index(i))
                    current_location = location
                    find_optimal_route(distance_list, 2, current_location)
                elif truck_number == 3:
                    third_truck.append(i)
                    third_truck_indices.append(i[1])
                    distance_list.pop(distance_list.index(i))
                    current_location = location
                    find_optimal_route(distance_list, 3, current_location)

first_truck_indices.insert(0, '0')

# Helpers to return needed value for truck 1.
# O(1)
def first_truck_index():
    return first_truck_indices

# O(1)
def first_truck_list():
    return first_truck


second_truck_indices.insert(0, '0')

# Helpers to return needed value for truck 2.
# O(1)
def second_truck_index():
    return second_truck_indices

# O(1)
def second_truck_list():
    return second_truck


third_truck_indices.insert(0, '0')

# Helpers to return needed value for truck 3.
# O(1)
def third_truck_index():
    return third_truck_indices

# O(1)
def third_truck_list():
    return third_truck
