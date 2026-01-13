# 	Check if a person is eligible to vote (age ≥ 18).
age = int(input("Enter your age:"))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
    
# Grade calculator based on marks: 90+ = A, 80+ = B, else C.
marks = int(input("Enter marks:"))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
else:
    print("Grade C")
    
# Simulate a traffic light: Red = Stop, Yellow = Wait, Green = Go.
signal = input("Enter traffic light color:")

if signal == "Red":
    print("Stop")
elif signal == "Yellow":
    print("Wait")
elif signal == "Green":
    print("Go")
else:
    print("Invalid signal")
    
    
# ATM withdrawal check: sufficient balance or not.
balance = 8000
withdraw = int(input("Enter withdrawal amount:"))

if withdraw <= balance:
    print("Transaction successful")
else:
    print("Insufficient balance")
    
# Check if a number is positive, negative, or zero.
num = int(input("Enter a number:"))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Nagative number")
else:
    print("Zero")
    
    
# Check if a number lies within a given range.
num = int(input("Enter a number:"))

if num > 10 and num < 50:
    print("Number is within range ")
else:
    print("Number is outside range")
    
# Username & password verification.
username = input("Enter username:")
password = input("Enter password:")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")
    
#Electricity bill calculator based on units consumed.
units = 120

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
else:
    bill = units * 10 
print("Electricity Bill: ",bill)
    
# Simple calculator (add, subtract, multiply, divide).
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
op = input("Enter operator(+,-,*,/):")

if op == "+":
    print("Result:",a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Ruslt:", a * b)
elif op == "/":
    print("Resuil:", a / b)
else:
    print("Invalid operator")

# Check type of triangle (equilateral, isosceles, scalene).
a = int(input("Enter side 1:"))
b = int(input("Enter side 2:"))
c = int(input("Enter side 3:"))

if a == b and b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
    