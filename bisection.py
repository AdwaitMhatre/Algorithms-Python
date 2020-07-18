def bisection(arr,want):
    start = 0
    stop = len(arr)-1
    while start <= stop:
        mid = (start + stop)//2
        if arr[mid] == want:
            return print(f"The number {want} was found in the list at index {mid} ")
        elif arr[mid] < want:
            start = mid + 1
        else:
            stop = mid - 1
    return print("Number not found in list")

# l = [1,2,3,4,5,6,7,8,9,10,11,12]
# bisection(l,12)

l = ["ayush","padwait","asdasdas","tdsfsdf","qweqwe","badsfa"]
l2 = sorted(l)
print(l2)
bisection(l2,"padwait")
