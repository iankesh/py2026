'''
Docstring for 30DOP.Day 02.exercise
This module contains exercises for Day 02 of the 30 Days of Python challenge.

1. Built in functions: abs(), len(), round(), type(), int(), float(), str(), __import__()
2. Built in keywords: False, None, pass, or
3. Variables and Constants
4. Input from user using input() function: name = input("Enter your name: ")
5. Casting: Converting one data type to another using int(), float(), str(), list(), tuple(), set(), dict()

    gravity = 9.81  # in m/s^2
    print(int(gravity))  # Convert float to int => 9
    print(float(9))     # Convert int to float => 9.0
    print(str(gravity)) # Convert float to str => '9.81'

    # str to list
    name = "Ankesh"
    name_list = list(name)
    print(name_list)  # ['A', 'n', 'k', 'e', 's', 'h']

    # str to tuple
    name_tuple = tuple(name)
    print(name_tuple)  # ('A', 'n', 'k', 'e', 's', 'h')

    # str to set
    name_set = set(name)
    print(name_set)  # {'A', 'n', 'k', 'e', 's', 'h'}

    # str to dict (using index as key)
    name_dict = {i: name[i] for i in range(len(name))}
    print(name_dict)  # {0: 'A', 1: 'n', 2: 'k', 3: 'e', 4: 's', 5: 'h'}

    # Importing math module using __import__()
    math_module = __import__('math')
    print(math_module.sqrt(16))  # 4.0

'''

first_name = "Ankesh"
last_name = "KedarNath"
full_name = first_name + " " + last_name
country = "India"
city = "Bengaluru"
age = 33
year = 2026
is_married = True
is_true = True
is_light_on = False
skills = ['Python', 'JavaScript', 'C++', 'Java', 'Go', 'Rust']
person_info = {'first_name': first_name,
               'last_name': last_name,
               'age': age,
               'country': country,
               'city': city}    

print("First Name:", first_name)
print("Last Name:", last_name)

print(type(first_name))      # str
print(type(age))             # int
print(type(is_married))      # bool
print(type(skills))          # list
print(type(person_info))     # dict

print("Length of first name:", len(first_name))
#compare the length of first name and last name
if len(first_name) > len(last_name):
    print("First name is longer than last name.")
elif len(first_name) < len(last_name):
    print("Last name is longer than first name.")
else:
    print("First name and last name are of equal length.")

num_one = input("Enter first number: ") or 10
num_two = input("Enter second number: ") or 2
remainder = int(num_one) % int(num_two)
print("Remainder of", num_one, "divided by", num_two, "is:", remainder)

PI=3.14  # Constant value of PI
radius = float(input("Enter radius of circle: ") or 10)
print("Area of circle with radius 10:", PI * radius**2)
print("Circumference of circle with radius 10:", 2 * PI * radius)