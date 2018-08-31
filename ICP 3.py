
# Write a python program to print the first letter of name using star symbols

    # Inputing a name as list

name = list(input("Please enter a name"))

    # Outputing the first letter
n=7
for i in range(n):

    # Inner for loop for logic execution
    for j in range((n // 2) + 1):

        # prints two column lines
        if ((j == 0 or j == n // 2) and i != 0 or

                # print first line of alphabet
                i == 0 and j != 0 and j != n // 2 or

                # prints middle line
                i == n // 2):
            print("*", end="")
        else:
            print(" ", end="")

    print()

#

print('*')

print('*'   '*')

print('*'   "*")

print('*''*''*''*')

print('*'      "*")

print('*'       "*")
print('*'        "*")
