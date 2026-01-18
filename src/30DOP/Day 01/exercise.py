'''
Docstring for 30DOP.Day 01.exercise
This module contains exercises for Day 01 of the 30 Days of Python challenge.

1. Installing python
2. Installing IDE
3. Data Types
    1. Numbers: -3,-2,0,1,2,3
    2. Strings: 'Ankesh", 'Python', '30 Days Of Python'
    3. Booleans: True, False
    4. Lists: Similar to Array in Java [1, 2, 3], ['a', 'b', 'c']
    5. Tuples: Collection of different types of data types, can not be modified once created (1, 2, 3), ('a', 'b', 'c')
    6. Sets: Not an ordered collection of items like list and tuple and only stores unique items {1, 2, 3}, {'a', 'b', 'c'}
    7. Dictionaries: Key Value Pair {'name': 'Ankesh'}, {'age': 25}
4. Check type of data types using type() function
'''

# Find euclidian distance between two points (2, 3) and (10, 8)
# Formula: d = √((x2 - x1)² + (y2 - y1)²)

import math
point1 = (2, 3)
point2 = (10, 8)
distance = math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)
print("Euclidian Distance:", distance)