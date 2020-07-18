def SelectionSort(arr):
    ref = 0
    while ref < len(arr):
        for num in range(ref,len(arr)):
            if arr[num] < arr[ref]:
                arr[num],arr[ref] = arr[ref],arr[num]
        ref = ref + 1
        print(arr)

l = [6,8,1,4,10,7,8,9,3,2,5]
SelectionSort(l)
