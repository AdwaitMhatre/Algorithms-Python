
def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x-1)
    print(ans)

y = int(input("Enter a number to calculate its factorial: "))
fact(y)

def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo(x-1)+fibo(x-2)

for i in range(0,11):
    print(fibo(i))
