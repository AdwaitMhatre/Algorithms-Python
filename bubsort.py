def BubbleSort(arr):
    swap_happened = True
    while swap_happened:
        print("iteration status: " + str(arr))
        swap_happened = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                swap_happened = True
                arr[i], arr[i+1] = arr[i+1], arr[i]


l = [6,8,1,4,10,7,8,9,3,2,5]
BubbleSort(l)
