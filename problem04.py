#PROBLEM STATEMENT 04
#Write a Python program to:
#• Store student records in a binary file.
#• Update marks of a given student.

import pickle
students = {}

#input
n = int(input("Enter number of students:"))
for i in range (n):
    name = input("Enter Student name:")
    marks = int(input("Enter Student marks:"))
    students[name] = marks
    
#save to file
with open ("students.dat", "wb") as f:
    pickle.dump(students, f)

#update to file
name = input("Enter student name to update marks:")
with open ("students.dat", "rb") as f:
    pickle.load(f)

if name in students:
    students[name] = float(input("Enter new marks:"))
    with open ("students.dat", "wb") as f:
        pickle.dump(students, f)
    print("Updated Successfully")
else:
    print("Student not found")

#display
print("\n RRecords")
for i in students:
    print(i, ":", students[i])