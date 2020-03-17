# TO-DO: Complete the selection_sort() function below 
def selection_sort(list_to_sort):
    x = 0
    while(x < len(list_to_sort)): 
        min = x
        for i in range(x + 1, len(list_to_sort)):
            #find minimum value and place it in the sorted sub-list
            if(list_to_sort[i] < list_to_sort[min]):
                min = i

        if(min != x):
            temp = list_to_sort[x]
            list_to_sort[x] = list_to_sort[min]
            list_to_sort[min] = temp

        print(list_to_sort)

        x += 1      

    return list_to_sort


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(list_to_sort):
    swap_occured = True #merely so the loop initiates
    i = 0 
    while(swap_occured):
        swap_occured = False
        for x in range(0, len(list_to_sort) - i - 1):
            if(list_to_sort[x] > list_to_sort[x+1]):
                temp = list_to_sort[x+1]
                list_to_sort[x+1] = list_to_sort[x]
                list_to_sort[x] = temp
                swap_occured = True

        print(list_to_sort)
        i += 1

    return list_to_sort


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr