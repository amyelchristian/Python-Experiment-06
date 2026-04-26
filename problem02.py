#PROBLEM STATEMENT 02
#Write a program to
#• Count Characters,
#• Words and
#• Lines

#taking input
str = input("Enter a sentence or paragraph:")

#logic to count characters, words and lines
characters = len(str)
words = str.split()
lines = str.splitlines()

#printing the logic
print("No. of characters:", characters)
print("No. of words:", len(words))
print("No. of lines:", len(lines)) 