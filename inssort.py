def InsertionSort(arr):
    for j in range(1,len(arr)):
        if arr[j] < arr[j-1]:
            i = j
            while i > 0:
                if arr[i] < arr[i-1]:
                    arr[i],arr[i-1] = arr[i-1],arr[i]
                i -= 1
            print(arr)


l = [6,8,1,4,10,7,8,9,3,2,5]
InsertionSort(l)
