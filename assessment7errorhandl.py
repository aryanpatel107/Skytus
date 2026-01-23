# Write a program to handle division by zero error.

print("1:")
try:
    a = 10
    b = 0
    result = a/b
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed ")
    
# Write a program to handle invalid integer input.

print("2:")
try:
    num = int(input("Enter a number:"))
    print("You entered: ",num)
except ValueError:
    print("Error: Invaild integer input")
    
# Write a program to open a file and handle the “file not found” error.

print("3;")
try:
    file = open("data.txt","r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Error: File not found")
    
# Write a program to demonstrate multiple exception blocks.

print("4:")
try:
    x = int(input("Enter number:"))
    y = int(input("Enter another number:"))
    print(x / y)
except ValueError:
    print("Enter: Invalid input")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
    
    
# Write a program to use finally for resource cleanup.

print("5:")
try:
    file = open("sample.txt", "w")
    file.write("Hello")
except IOError:
    print("File error")
finally:
    file.close()
    print("File closed")
    
    
# Write a program to create a custom exception for invalid age (<18).

print("6:")
class InvaildageError(Exception):
    pass

try:
    age = int(input("Enter age:"))
    if age < 18:
         raise InvaildageError(" Age must be 18 or above ")
    print("Access granted")
except InvaildageError as e:
    print(e)
    
    
# Write a program to handle IndexError when accessing a list.

print("7:")
try:
    number = [1,2,3]
    print(number[5])
except IndexError:
    print("Error : Index out of range")
    
    
# Write a program that takes two numbers and handles all possible errors.

print("8:")
try:
    
  a = int(input("Enter first number:"))
  b = int(input("Enter second number:"))
  print("Result:", a / b)

except Exception as e:
    print("Error:", e)
    

# Write a program to log errors to a file instead of printing them.

print("9:")
import logging 
logging.basicConfig(filename="error.log", level = logging.ERROR)

try:
    x = 10 / 0
except Exception as e:
    logging.error(e)
    
    
# Write a program that validates an email format and raises an exception for invalid ones.

print("10:")
import re

class InvalidEmailError(Exception):
    pass

try:
    email = input("Enter email:")
    pattern = r"[\w.-]+@[\w.-]+\.\w+$"
    
    if not re.match(pattern, email):
        raise InvalidEmailError("Invalid email format")
    print("Valid email")
except InvalidEmailError as e:
    print(e)
    