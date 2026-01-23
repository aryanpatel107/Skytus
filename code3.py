# Take a string input and print its length.
print("1:")
s = input("Enter a string:")
print(len(s))
# Convert a sentence to lowercase.
print("2:")
sentence = input("Enter a sentence: ")
print(sentence.lower())

# Replace spaces with underscores in a string.
print("3:")
text = input("Enter a string: ")
print(text.replace(" ", "_"))


# Extract the first and last character of a string.
print("4:")
text = input("Enter a string: ")
print("First character:", text[0])
print("Last character:", text[-1])

# Reverse a string using slicing.
print("5:")
text = input("Enter a string: ")
print("Reversed string:", text[::-1])

# Count how many times a letter appears in a string.
print("6:")
text = input("Enter a string: ")
letter = input("Enter a letter to count: ")
print("Count:", text.count(letter))

# Check if a word is present in a sentence.
print("7:")
sentence = input("Enter a sentence: ")
word = input("Enter a word to search: ")

if word in sentence:
    print("Word found")
else:
    print("Word not found")

# Take name & age and print using f-string formatting.
print("8:")
name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"My name is {name} and I am {age} years old.")

# Remove extra spaces from the start and end of a string.
print("9:")
text = input("Enter a string with spaces: ")
print(text.strip())

# Join a list of words into a single string with - between them
print("10:")
words = ["Python", "is", "easy"]
sentence = "-".join(words)
print(sentence)


# python string handaling code3.1




# Create a list of your 5 favorite movies.
print("11:")
movies = ["Avatar", "Titanic", "Joker", "Inception", "Dangal"]
print(movies)

# Add a new movie to the list.
print("12:")
movies.append("Pathaan")
print(movies)

# Remove the first movie from the list.
print("13:")
movies.pop(0)
print(movies)

# Sort a list of numbers in ascending order.
print("14:")
numbers = [5, 2, 9, 1, 3]
numbers.sort()
print(numbers)

# Reverse a list.
print("15:")
numbers.reverse()
print(numbers)

# Find the largest number in a list.
print("16:")
numbers = [10, 50, 30, 70, 20]
print(max(numbers))

# Merge two lists into one.
print("17:")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
new_list = list1 + list2
print(new_list)

# Access the last element of a list without using index number.
print("18:")
fruits = ["apple", "banana", "mango"]
print(fruits[-1])


# Create a nested list and access a specific inner element.
print("19:")
marks = [[10, 20, 30], [40, 50, 60]]
print(marks[1][2])

# Count how many times an element appears in a list.
print("20:")
numbers = [1, 2, 3, 2, 4, 2]
print(numbers.count(2))



