# Question 3

# Question 3 (Part 1)
# You have to define a function named students and pass a parameter to that function which takes a list of students name(don't use the List)

# Question 3 (Part 2)
# You have to define a function named isGreaterThan20 in which you have to pass two parameters to the function and the first parameter by default should be 20.

# Arbitrary Arguments
def student(*name):
    for name in name:
        print(name)
student("Neha","Devyani","Gayatri","Rutuja","Alpana","Mayuri","Muskan","Varsha")



