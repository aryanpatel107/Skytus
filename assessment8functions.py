# Function to check if a number is prime.


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
print(is_prime(7))
    
    
# Function to reverse a string.


def reverse_string(s):
    return s[::-1]

print(reverse_string("Aryan"))



# Function to find factorial.

def factorial(n):
    fact = 1
    
    for i in range(1, n +1):
        fact *= i
    return fact
print(factorial(5))
    
    
    
# Function to calculate simple interest.


def simple_interest(p, r, t):
    return(p *r *t ) / 100

print(simple_interest(1000, 5, 2))



# Function to check if a word is palindrome.


def is_pailndrome(word):
    return word == word[::-1]

print(is_pailndrome("madam"))


    
# Function to count vowels in a string.


def count_vowels(s):
    vowels = "lifeisrace"
    count = 0
    for char in s:
        if char in vowels:
             count += 1
    return count
    
print(count_vowels("Python Programming"))
    
    
    
    
# Function to merge two lists.


def merge_lists(list1, list2):
    return list1 + list2

print(merge_lists([1, 2], [3, 4]))




# Function to find GCD of two numbers.


def gcd(a, b):
    while b !=0:
        a, b = b, a % b
    return a
    
print(gcd(12, 18))
    
    
    
# Function to find area of rectangle.


def area_rectangle(length, width):
    return length * width

print(area_rectangle(5, 4))



# Function to check Armstrong number.	


def is_armstrong(n):
    temp = n
    sum = 0
    digits = len(str(n))
    
    
    while temp > 0:
        digit = temp % 10
        sum += digit ** digits
        temp //= 10
        
    return sum == n
    
print(is_armstrong(153))
    