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

# Join a list of words into a single string 
print("10:")
words = ["Python", "is", "easy"]
sentence = " ".join(words)
print(sentence)

