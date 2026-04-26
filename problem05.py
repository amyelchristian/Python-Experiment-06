#PROBLEM STATEMENT 05
#WAP to:
#a) Read number from a text file
#b) Store odd number in another binary file

import pickle

#input
filename = input("Enter the text file:")

#read number from a text file
with open ("filename", "r") as f:
    numbers = f.read().split()

#store odd number in a binary file
odd = []
for i in numbers:
    if int(i) % 2 != 0:
        odd.append(int(i))
with open ("odd.dat", "wb") as f:
    pickle.dump(odd, f)

#print
print("Odd numbers:", odd)