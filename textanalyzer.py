'''
This a mini project, showing a program that analyzes a sample file to find what percentage of the text each character occupies.
'''

#Open and read file

filename = input("Enter a filename:")

with open(filename) as f:
    text = f.read()


#Count how many times a character occurs in a string

#This function takes as its arguments the text of the file and one character, returning the number of times that character appears in the text.

def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

#Find the percentage of the tex each character of the alphabet occupies

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100* count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))