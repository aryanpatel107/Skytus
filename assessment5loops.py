# Print numbers from 1 to 10.
print("A1:")
for i in range(1,11):
    print(i)
    
# Display multiplication table for a given number.
print("A2:")
num = int(input("Enter a number:"))

for i in range(1,11):
    print(num,"x",i,"=", num*i)
    
# Find factorial of a number.
print("A3:")
num = int(input("Enter a number:"))
fact = 1
for i in range(1,num + 1):
    fact = fact*i
    print("Factorial:", fact)

# Generate the first N Fibonacci numbers.

print("A4:")
n = int(input("Enter number to terms:"))
a,b = 0,1

for i in range(n):
    print(a,end=" ")
    
    a, b = b, a+b
    
# Check if a number is prime.
print(" ")

print("A5:")
num = int(input("Enter a number:"))

if num <= 1:
    print("Not a prime number")
else:
    for i in range(1,num):
        if num % i == 0:
            print("Not a prime number")
            break
        else:
            print("Prime number")
            
# Reverse a number (e.g., 123 → 321).
print("A6:")
num =1234
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
    print("Reversed number:", rev)
    
# Count digits in a number.
print("A7:")
num = int(input("Enter a number:"))
count = 0

while num > 0:
    count += 1
    num = num // 10
    print("Number of digits:", count)
    
# Find sum of even numbers between 1–100.
print("A8:")
sum_even = 0

for i in range(1,101):
    if i % 2 == 0:
        sum_even += i
        print("Sum of even number:",sum_even)
        
# Print a pyramid pattern.
print("A9:")
rows = int(input("Enter a number of rows:"))
 
for i in range(1, rows + 1):
    print("*" * i)
     
# Find all divisors of a number.
print("A10:")
num = int(input("Enter a number:"))

print("Divisors are:")
for i in range(1,num + 1):
    if num % i == 0:
        print(i)
        