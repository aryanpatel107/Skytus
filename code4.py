# Create a tuple with 5 numbers.
print("1:")
numbers = (10, 20, 30, 40, 50)
print(numbers)

# Access the third element in a tuple.
print("2:")
print(numbers[2])

# Unpack a tuple into separate variables.
print("3:")
a, b, c, d, e = numbers
print(a, b, c, d, e)

# Create a set of 5 fruits.
print("4:")
fruits = {"apple", "banana", "mango", "orange", "grape"}
print(fruits)

# Add a new fruit to the set.
print("5:")
fruits.add("pineapple")
print(fruits)


# Remove an element from a set.
print("6:")
fruits.remove("banana")
print(fruits)

# Find union of two sets.
print("7:")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1.union(set2)
print(union_set)

# Find intersection of two sets.
print("8:")
intersection_set = set1.intersection(set2)
print(intersection_set)

# Check if one set is subset of another.
print("9:")
A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))

# Convert a list with duplicate
print("10 :")
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(my_list)

print(unique_set)




# Python Data Structures 4.1
print("Python Data Structures (4.1 )  ")
# Create a dictionary storing student names and marks.
print("11:")
students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92
}
print(students)



# Add a new key-value pair to an existing dictionary.
print("12:")
students["David"] = 88
print(students)

# Delete a key-value pair from a dictionary.
print("13:")
del students["Bob"]
print(students)

# Merge two dictionaries into one.
print("14:")
dict1 = {"Math": 90, "Science": 85}
dict2 = {"English": 88, "History": 80}

merged_dict = dict1 | dict2
print(merged_dict)

# Check if a key exists in a dictionary.
print("15:")
students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92
}
print(students)

print("Alice" in students)

# Count word frequency in a given string using a dictionary.
print("16:")
text = "apple banana apple mango banana apple"
words = text.split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)


# Find the key with the maximum value in a dictionary.
print("17:")
scores = {"Alice": 85, "Bob": 78, "Charlie": 92}

max_key = max(scores, key=scores.get)
print(max_key)

# Reverse keys and values in a dictionary.
print("18:")
original = {"a": 1, "b": 2, "c": 3}

reversed_dict = {value: key for key, value in original.items()}
print(reversed_dict)

# Update the value for a specific key.
print("19:")
students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92
}

print(students)

students["Alice"] = 90
print(students)

# Convert a list of tuples into a dictionary
print("20:")
tuple_list = [("a", 1), ("b", 2), ("c", 3)]

converted_dict = dict(tuple_list)
print(converted_dict)

