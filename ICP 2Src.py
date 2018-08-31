
infile = open('myfile', 'r')

sum = 0.0

count = 0

# To read the lines of the file
line = infile.readline()

#The use of while loop to to go through lines  and woords in the file
while line!="":
    for xStr in line:
        count = 0.0
        count = count + 1
        line = infile.readline()

    print("letters number "+str(count))
infile.close()

line = infile.readline()
while line!="":
    count = 0.0
    for xStr in line.split(' '):
        count = count + 1
    line = infile.readline()
    print("The number of words is:" +str(count))