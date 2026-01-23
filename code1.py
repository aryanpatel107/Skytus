# 	1. Write a program to print your name, age, and city in one line.
print ("1:")
name = "Aryan Patel"
age = 20
city = "Bilimora"

print (name)
print (age)
print (city)
print ("")





# 2. Take user input for two numbers and print their sum.
print ("2:")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print ("Sum of ",num1+num2)
print ("")






# 3. Write a program to convert temperature from Celsius to Fahrenheit.
print("3:")
celsius = float(input("Enter temprature in Celsius:"))
fahrenheit = (celsius * 9/5) + 32

print("Teamprature in falhrenheit:",fahrenheit)
print("")




# 4. Store your name in a variable and print it in uppercase
print ("4:")
name = "Aryan Patel"
print("Upper Case",name.upper())
print ("")
# 5. Ask the user for their birth year and calculate their current age.
print("5:")
birth_yr = 2005
current_yr = 2026

Age_calc=current_yr - birth_yr
print ("Age",Age_calc)
print ("")

# 6. Write a program to swap the values of two variables.
print ("6:")
a=1
b=2
print ("Before Swap:",a,b)

temp = a
a = b
b = a
print("After Swap",a,b)
print("")

# 7. Create a program to calculate the area of a rectangle from user inputs.
print("7:")
length = float(input("Length: "))
width = float(input("Width: "))

area = length * width
print("Area of rectangle:", area)
print("")
# 8. Write a program to check if a number is positive or negative.
print("8:")
num = int(input ("Enter number:"))
if(num >= 0):
    print("Enter number is positive")
else:
    print("Enter number is nagative")

# 9. Ask for two numbers and print their average
print("9:")
average = a+b/2
print(average)
print("")