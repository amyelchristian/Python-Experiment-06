#PROBLEM STATEMENT 01
#Write a program to accept string/sentences from the user till the user enters "END" to. 
# Save the data in a text file and then display only those sentences which begin with an uppercase alphabet.

sentences = []

#taking the input from the user
while True:
    s = input("Enter a sentence or type ('END') to stop:")
    if s == 'END':
        break
    sentences.append(s)
    
#saving the data to the file
with open ("sentences.txt", "w") as f:
    for line in sentences:
        f.write(line + "\n")

#reading the file
with open ("sentences.txt", "r") as f:
    for line in sentences:
        if line [0].isupper():
            print(line.strip())
