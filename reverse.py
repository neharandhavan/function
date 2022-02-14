# reverse function print the reverse order of the list.

# Input:-

# reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
# Output :-
# reverse_list = ["D", "R", "A", "M", "E", "B", "A", "A", "Z"]




def reverse(reverse_list):
    i=0
    while i<len(reverse_list):
        print(reverse_list[-i-1])
        i+=1
reverse(["Z", "A", "A", "B", "E", "M", "A", "R", "D"])        