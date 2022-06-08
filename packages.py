# Empty lists for each type of data collection needed.
import distances
import csv_reader

# Create empty lists to hold values associated with the delivery times and distances of all packages.
first_delivery = []
second_delivery = []
third_delivery = []
first_truck_route_distance = []
second_truck_route_distance = []
third_truck_route_distance = []

# These are the times that I have decided will be the most efficient times for each truck to leave the hub
truck_one_departure_time = ['8:00:00']
truck_two_departure_time = ['9:05:00']
truck_three_departure_time = ['10:20:00']

# Set the delivery start times
# O(n)
for index, value in enumerate(csv_reader.get_first_delivery()):
    csv_reader.get_first_delivery()[index][9] = truck_one_departure_time[0]
    first_delivery.append(csv_reader.get_first_delivery()[index])

# Compare the addresses from truck one to the address list.
# O(n^2)
for index, outer in enumerate(first_delivery):
    for inner in distances.retrieve_address():
        if outer[2] == inner[2]:
            first_truck_route_distance.append(outer[0])
            first_delivery[index][1] = inner[0]

# Call algorithm for first truck to sort packages
distances.find_optimal_route(first_delivery, 1, 0)
first_truck_total = 0

# Get total distance for all packages for truck 1.
# O(n)
for index in range(len(distances.first_truck_index())):
    try:
        first_truck_total = distances.get_distance(int(distances.first_truck_index()[index]),
                                                   int(distances.first_truck_index()[index + 1]),
                                                   first_truck_total)
        deliver_packages = distances.get_truck_time(
            distances.retrieve_current_distance(int(distances.first_truck_index()[index]),
                                                int(distances.first_truck_index()[index + 1])),
            truck_one_departure_time)
        distances.first_truck_list()[index][10] = (str(deliver_packages))
        csv_reader.get_hash_table().update(int(distances.first_truck_list()[index][0]), first_delivery)
    except IndexError:
        pass

# Set delivery start time for truck 2
# O(n)
for index, value in enumerate(csv_reader.get_second_delivery()):
    csv_reader.get_second_delivery()[index][9] = truck_two_departure_time[0]
    second_delivery.append(csv_reader.get_second_delivery()[index])

# Compare the addresses from truck two to the address list.
# O(n^2)
for index, outer in enumerate(second_delivery):
    for inner in distances.retrieve_address():
        if outer[2] == inner[2]:
            second_truck_route_distance.append(outer[0])
            second_delivery[index][1] = inner[0]

# Call algorithm for second truck to sort packages
distances.find_optimal_route(second_delivery, 2, 0)
second_truck_total = 0

# Get total distance for all packages for truck 2.
# O(n)
for index in range(len(distances.second_truck_index())):
    try:
        second_truck_total = distances.get_distance(int(distances.second_truck_index()[index]),
                                                    int(distances.second_truck_index()[index + 1]),
                                                    second_truck_total)
        deliver_packages = distances.get_truck_time(
            distances.retrieve_current_distance(int(distances.second_truck_index()[index]),
                                                int(distances.second_truck_index()[index + 1])),
            truck_two_departure_time)
        distances.second_truck_list()[index][10] = (str(deliver_packages))
        csv_reader.get_hash_table().update(int(distances.second_truck_list()[index][0]), second_delivery)
    except IndexError:
        pass

# Set delivery start time for truck 3
# O(n)
for index, value in enumerate(csv_reader.get_third_delivery()):
    csv_reader.get_third_delivery()[index][9] = truck_three_departure_time[0]
    third_delivery.append(csv_reader.get_third_delivery()[index])

# Compare the addresses from truck three to the address list.
# O(n^2)
for index, outer in enumerate(third_delivery):
    for inner in distances.retrieve_address():
        if outer[2] == inner[2]:
            third_truck_route_distance.append(outer[0])
            third_delivery[index][1] = inner[0]

# Call algorithm for third truck to sort packages
distances.find_optimal_route(third_delivery, 3, 0)
third_truck_total = 0

# Get total distance for all packages for truck 3.
# O(n)
for index in range(len(distances.third_truck_index())):
    try:
        third_truck_total = distances.get_distance(int(distances.third_truck_index()[index]),
                                                   int(distances.third_truck_index()[index + 1]),
                                                   third_truck_total)
        deliver_packages = distances.get_truck_time(
            distances.retrieve_current_distance(int(distances.third_truck_index()[index]),
                                                int(distances.third_truck_index()[index + 1])),
            truck_three_departure_time)
        distances.third_truck_list()[index][10] = (str(deliver_packages))
        csv_reader.get_hash_table().update(int(distances.third_truck_list()[index][0]), third_delivery)
    except IndexError:
        pass

# Sums the distances from all trucks into a total distance to represent the efficiency of the delivery route.
# O(1)
def wgups_total_distance():
    return first_truck_total + second_truck_total + third_truck_total
