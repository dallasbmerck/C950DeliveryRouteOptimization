# DeliveryRouteOptimization
- Author: Dallas Merck
- University Data Structures and Algorithms Project

## Development Environment:
- IDE: PyCharm Community Edition 2022.1
- Language: Python

## Description:
- Delivery route optimization for a contrived company consisting of 3 trucks and two delivery drivers.
- Delvery route scenario consists of 26 addresses and 40 packages. 
- Each package has a specific attribute such as: must be delivered before a certain time, delayed in flight to facility, must be delivered with another package, and must be on a specific truck.
- Utilized a chaining hash table as the data structure. 
- Algorithm used to find most optimal route is a greedy heuristic with a time complexity of O(n^2).

## Outcome:
- Requirement of the project was to yield a total distance traveled less than 140 miles.
- Route completed in 103 miles.
