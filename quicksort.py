def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less)+[pivot]+quicksort(greater)
myarray = [2,4,5,6,9,8,3,15,7,5]
print(quicksort(myarray))