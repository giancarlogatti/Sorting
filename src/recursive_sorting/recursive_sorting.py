# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    #arrA and arrB are sorted already
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    i = 0
    aIndex = 0
    bIndex = 0
    while(i < elements):
        if(bIndex >= len(arrB) or (aIndex < len(arrA) and arrA[aIndex] <= arrB[bIndex])):
            #take from aIndex and increment
            merged_arr[i] = arrA[aIndex]
            aIndex += 1
        else:
            merged_arr[i] = arrB[bIndex]
            bIndex += 1
        i += 1
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    size = len(arr)

    if(size == 0 or size == 1):
        return arr

    mid = int(size/2)
    
    #sort from start to mid point
    arrStartToMid = merge_sort(arr[0:mid])
    arrMidToEnd = merge_sort(arr[mid:])
    arr = merge(arrStartToMid, arrMidToEnd)   
    return arr

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
