def findsmallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1,len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index

def selectsort(array):
    newarray = []
    for i in range(len(array)):
        smallest_index = findsmallest(array)
        #newarray.append(array.pop(smallest_index))
        newarray.append(array[smallest_index])
        array.pop(smallest_index)
        #print(array)
        #print(newarray)
    return newarray

myarray = [5,6,4,8,2,9,3,1,7]
print(selectsort(myarray))