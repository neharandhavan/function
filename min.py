#  Use the min function and find the minimun value of the list.


 
# list = [8, 6, 4, 8, 4, 50, 2, 7]
# Output :-2



def min(list):
    i=0
    min=4
    while i<len(list):
        if list[i]<min:
            min=list[i]
        i+=1
    print(min)
min([8, 6, 4, 8, 4, 50, 2, 7])




