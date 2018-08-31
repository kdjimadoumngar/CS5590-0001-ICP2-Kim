

# Writing a python program to take a list of numbers as input and retrurn a tuple of first and last numbers in the list

# The list of integer number

#import numpy as np

my_list = [1,2,3,4,5]


# To output the first and last numbers

print(my_list[0][4])


#print(my_list)

# print(my_list['1','5'])


#type(my_list)


# 2. Writing a python program to count number of words and characters in a file and print the output

    # To input the file

fname = input("Enter the file name: ")
    # To initialize the count
number_words = 0 # Number of words
number_char = 0  # Number of charatcers

    # To open the file in reading mode with open() function
with open(fname, 'r') as f:

    # The use of for loop to to go through lines  and woords in the file
    for line in f:
        words = line.split()
        number_words += length(words) # The number of words in the line is counted using the len() and there is an incrementation of the counts
        for words in f:
            char = words.split()
            number_char += length(char) # The number of characters in the words is counted using the len() and there is an incrementation of the counts

    # To print the number of words and characters

print("The number of words is :") # Printing the number of words

print("The number of characters is:") # Printing the number of characters





# Write a python program to print the first letter of name using star symbols

    # Inputing a name as list

name = list(input("Please enter a name"))

    # Outputing the first letter

first_letter = name[0]
