import string
import random
import time

def gen_name(length):
    return "".join(random.choice(string.ascii_letters) for i in range(length))

domains = ["xyz.com","abc.com","lmn.com","pqr.com"]

def gen_domain(domains):
    return random.choice(domains)

def gen_email(length,domains,total):
    emails = []
    for i in range(total):
        emails.append(gen_name(length)+"@"+gen_domain(domains))
    return emails

def bisection(arr,want):
    start = 0
    stop = len(arr)-1
    while start <= stop:
        mid = (start + stop)//2
        if want == arr[mid]:
            return f"Email {want} found at index {mid}"
        elif want > arr[mid]:
            start = mid + 1
        elif want < arr[mid]:
            stop = mid - 1
    return f"Email {want} not found in list"

def runtime(func_name, *args):
    ini = time.time()
    func_name(*args)
    fin = time.time()
    diff = fin-ini
    return print(f"{func_name.__name__}\tTime elapsed ---> {diff:.5f} sec")

list = gen_email(10,domains,1000000)
email = "adwaitmhatre77@gmail.com"
list.append(email)
list2 = sorted(list)
print(bisection(list2,email))
print("-"*50)
runtime(bisection,list2,email)
runtime(gen_email,10,domains,1000000)
