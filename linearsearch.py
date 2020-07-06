def binarysearch(array,numberofindex,x):
    start = 0
    end = n - 1
    while (start <= end):
        middle_number = (start + end)//2
        if (array[middle_number]) == x:
            return middle_number
        elif (x < array[middle_number]):
            end = middle_number - 1
        else:
            start = middle_number + 1
    return -1  
