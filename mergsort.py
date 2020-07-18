def merge_sort(arr1,arr2):
    i = 0
    j = 0
    sorted_list = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_list.append(arr1[i])
            i += 1
        else:
            sorted_list.append(arr2[j])
            j += 1
    while i < len(arr1):
        sorted_list.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_list.append(arr2[j])
        j += 1
    return sorted_list

def divide(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr)//2
        l1 = divide(arr[:middle])
        l2 = divide(arr[middle:])
        return merge_sort(l1,l2)

l = [6,8,1,4,10,7,8,9,3,2,5]
print(divide(l))
