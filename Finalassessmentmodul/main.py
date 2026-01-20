# 1. Create a custom math module and import it in another file.

import mymath


print("Addition:", mymath.add(10, 5))
print("Subtraction:", mymath.subtract(10, 3))






# 2. Create a module to perform string operations. 

import string_ops

text = "Python Programming"

print("Original String:", text)
print("Uppercase:", string_ops.to_upper(text))
print("Lowercase:", string_ops.to_lower(text))
print("Reversed:", string_ops.reverse_string(text))
print("Length:", string_ops.string_length(text))


# 3. Use random module to generate 5 random integers.

import random

print("Generting 5 random integers between 1 and 100:")

for i in range(5):
    number = random.randint(1, 100)
    print(number)



# 4. Use datetime module to display current date and time.

from datetime import datetime

current_time = datetime.now()

print("Current Date and Time:", current_time)

print("Formatted Date & Time:", current_time.strftime("%y-%M-%d %H:%M:%S"))



# 5. Use math module to find factorial of a number. 

import math

num = int(input("Enter number to find its factorial:"))

fact = math.factorial(num)

print(f"The factorial of {num} is:{fact}")


# 6. Create a package shapes with modules for circle and rectangle.
 
from shapes import circle, rectangle

r = 5
l = 10
w = 4

print("Circle Area:", circle.area(r))
print("Circle Circumference:", circle.circumference(r))

print("Rectangle Area:", rectangle.area(l, w))
print("Rectangle Perimeter:", rectangle.perimeter(l, w))


 
 
# 7. Import multiple functions from one module and use them. 




from shapes.circle import area, circumference

radius = 7

circle_area = area(radius)
circle_circumference = circumference(radius)

print(f"Circle with radius {radius}:")
print("Area:", circle_area)
print("Circumference:", circle_circumference)





# 8. Write a program to shuffle a list using random module.

import random


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Original list:", my_list)


random.shuffle(my_list)

print("Shuffled list:", my_list)



# 9. Write a program to calculate the difference between two dates.

from datetime import datetime


date1_str = input("Enter the first date (YYYY-MM-DD): ")
date2_str = input("Enter the second date (YYYY-MM-DD): ")


date_format = "%Y-%m-%d"
date1 = datetime.strptime(date1_str, date_format)
date2 = datetime.strptime(date2_str, date_format)


difference = date2 - date1


print(f"The difference between {date2_str} and {date1_str} is {difference.days} days.")


# 10. Use os module to list files in a directory.	

import os


directory = "."  


all_items = os.listdir(directory)


files = [f for f in all_items if os.path.isfile(os.path.join(directory, f))]

print("Files in the directory:")
for file in files:
    print(file)
