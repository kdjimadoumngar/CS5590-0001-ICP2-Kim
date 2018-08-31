
# Open an input file

infile = open('myfile', 'r')

# Initialization of counts and sum of characters in words

sum = 0.0

count = 0

# To read the lines of the file
line = infile.readline()

#The use of while loop to to go through lines  and woords in the file
while line!="":
    sum = sum + len(line.split())
    for xStr in line:

        count = count + 1
    line = infile.readline()
# Printing the number of characters
print("letters number "+str(count))
# Printing the

print("The number of words is:" +str(sum))