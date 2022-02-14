# Question 4

# This question is in 2 parts. Submit the code of both the parts by writing them in the same file.

# Question (Part 1)
# Write a function named add_numbers which takes two numbers as arguments and then prints their sum.
# The name of the arguments should be number1 and number2.

# Input :-

# # Write add_numbers function here
# num1 = 56
# num2 = 12
# add_numbers(num1,num2)


def add_number(num1,num2):
    print(num1+num2)
add_number(56,12)



# Question (Part 2)

# Write a function named add_numbers_list which takes 2 lists of two integers and then prints the sum of the integers with the same position.

# Use the add_numbers function given in Part 1 to count 2 integers that have the same position.

# If we give [50, 60, 10] and [10, 20, 13] to this function it will print this



def add_numbers_list():
    a=[50, 60, 10]
    b=[10, 20, 13]
    i=0
    n=[]
    while i<len(a):
        x=a[i]+b[i]
        n.append(x)
        i+=1
    print(n)
add_numbers_list()        
    

