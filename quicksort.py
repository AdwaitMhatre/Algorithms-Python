def quick(arr):
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
        return quick(small) + equal + quick(large)

l = [6,8,1,4,10,7,8,9,3,2,5]
print(quick(l))
