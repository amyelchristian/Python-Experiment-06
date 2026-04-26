#PROBLEM STATEMENT 03
#Write a python Program to:
#• Read a text file
#• Search for a given word
#• Display the number of times it occurs.

#taking input from the user
filename = input("Enter the filename:")
search = input("Enter the word to search:")

#logic
with open ("filename", "r") as f:
    word = f.read()

count = word.lower.split.count(word.lower())

#print
print("The number of times the word occurs is:", count)