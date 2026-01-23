# Write a program to read a file and display its contents.
file = open("sample.txt", "w")
file.write("Hello")
file.close()
file = open("sample.txt", "r")
conent = file.read()
print(conent)
file.close()



# Write a program to count the number of lines in a file.

file = open("sample.txt","r")
lines = file.readlines()
print("Number of lines:",len(lines))
file.close()



# Write a program to count how many times each word appears in a file.

file = open("sample.txt","r")
words = file.read().split()
file.close()

words_count = {}
for word in words:
    words_count[word] = words_count.get(word, 0) + 1
    
    print(words_count)
    
    


# Write a program to write 5 user-entered sentences to a file.

file = open("sentences.txt","w")

for i in range(5):
    sentence = input("Enter sentence:")
    file.write(sentence + "\n" )
    
file.close()
    
    

# # Write a program to append a list of strings to an existing file.

lines = ["Apple\n","Banana\n", "Cherry\n"]

file = open("fruits.txt","a")
file.writelines(lines)

file.close()



# Write a program to read a file and print only lines containing a specific word.

file = open("sample.txt", "r")

for line in file:
    if "Python" in line:
        print(line.strip())
        
file.close()



        
# Write a program to replace a specific word in a file and save changes.

file = open("sample.txt", "r")
conent = file.read()
file.close()

content = conent.replace("Python","Java")

file = open("sample.txt","w")
file.write(conent)
file.close()



# Write a program to merge the contents of two text files into a third file.
file = open("file1.txt", "w")
file.write("Welcome to Python")
file.close()
file = open("file2.txt", "w")
file.write("Python is easy")
file.close()
file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")
file3 = open("merged.txt", "w")

file3.write(file1.read())
file3.write(file2.read())

file1.close()
file2.close()
file3.close()



# Write a program to read a CSV file and display its content in a formatted way.

import csv


with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "Age"])
    writer.writerow([1, "Alice", 20])
    writer.writerow([2, "Bob", 22])
    writer.writerow([3, "Charlie", 21])

print("data.csv file created successfully")

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(" | ".join(row))


# Write a program to back up a file by copying its contents into another file.	
file = open("original.txt", "w")

file.write("This is the original file.\n")
file.write("It contains important data.\n")
file.write("This file will be used for backup.\n")
file.write("Python file handling example.\n")

file.close()

print("original.txt file created successfully")

source = open("original.txt", "r")
backup = open("backup.txt", "w")

backup.write(source.read())

source.close()
backup.close()
