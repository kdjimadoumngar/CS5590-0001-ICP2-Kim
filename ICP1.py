# Input a list of numbers
inp = input('Please enter your numbers')

# Create a list
my_list = inp.split(',')

# Transform the list to a tuple

tuple = tuple(my_list)


# To output the first and last numbers

print((tuple[0],tuple[-1]))
