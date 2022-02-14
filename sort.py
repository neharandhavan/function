# # sorted


# # Using sort function sort the given list.

# Input:-

# unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]

# Output :-
# unorder_list = [0, 3, 4, 6, 7, 8, 9, 15, 34, 56]


# from re import A


def sort(unorder_list):
    i=0
    while i<len(unorder_list):
        j=0
        while j<len(unorder_list):
            if unorder_list[j] > unorder_list[i] :
                temp = unorder_list[i]
                unorder_list[i] = unorder_list[j]
                unorder_list[j] = temp
            j+=1
        i+=1
    print(unorder_list)
sort([6, 8, 4, 3, 9, 56, 0, 34, 7, 15])



