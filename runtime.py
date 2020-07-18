import random
import time
import sys

sys.setrecursionlimit(10**6)

def BubbleSort(arr):
    swap_happened = True
    while swap_happened:
        swap_happened = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                swap_happened = True
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

def SelectionSort(arr):
    ref = 0
    while ref < len(arr):
        for num in range(ref,len(arr)):
            if arr[num] < arr[ref]:
                arr[num],arr[ref] = arr[ref],arr[num]
        ref = ref + 1
    return arr

def InsertionSort(arr):
    for j in range(1,len(arr)):
        if arr[j] < arr[j-1]:
            i = j
            while i > 0:
                if arr[i] < arr[i-1]:
                    arr[i],arr[i-1] = arr[i-1],arr[i]
                i -= 1
    return arr

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

def Divide(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr)//2
        l1 = Divide(arr[:middle])
        l2 = Divide(arr[middle:])
        return merge_sort(l1,l2)

def QuickSort(arr):
    if len(arr) < 2:
        return arr

    else:
        ref = arr[-1]
        small, equal, large = [], [], []
        for num in arr:
            if num < ref:
                small.append(num)
            elif num == ref:
                equal.append(num)
            else:
                large.append(num)
        return QuickSort(small) + equal + QuickSort(large)


print("-Algoritm Runtime Analyzer-")
x = int(input("Enter the number of integers you want: "))
y = int(input("Enter the upper limit of the range you want: "))
z = int(input("Enter the number of runs: "))
print("-"*50)

for i in range(z):
    list = [random.randint(1,y) for i in range(x)]

    ini1 = time.time()
    BubbleSort(list)
    fin1 = time.time()
    print(f"BubbleSort Time Elapsed --> \t {fin1-ini1:.5f} sec")

    ini2 = time.time()
    SelectionSort(list)
    fin2 = time.time()
    print(f"SelectionSort Time Elapsed --> \t {fin2-ini2:.5f} sec")

    ini3 = time.time()
    sorted(list)
    fin3 = time.time()
    print(f"Inbuilt Sorting Time Elapsed --> {fin3-ini3:.5f} sec")

    ini4 = time.time()
    QuickSort(list)
    fin4 = time.time()
    print(f"QuickSort Time Elapsed --> \t {fin4-ini4:.5f} sec")

    ini5 = time.time()
    Divide(list)
    fin5 = time.time()
    print(f"MergeSort Time Elapsed --> \t {fin5-ini5:.5f} sec")

    print("-"*50)
