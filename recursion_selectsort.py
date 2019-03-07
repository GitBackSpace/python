def findsmallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1,len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index

newarray = []
def selectsort(array):
    if len(array) < 1:
        return newarray
    else:
            smallest_index = findsmallest(array)
            newarray.append(array.pop(smallest_index))
            return selectsort(array)

myarray = [5,6,4,8,2,9,3,1,7,8]
print(selectsort(myarray))