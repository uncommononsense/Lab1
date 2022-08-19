n = int(input("enter n: "))

def fac(n):
    print(n)
    if n < 0 or (n - int(n) != 0):
        print("please enter a valid number")
    if n == 0 or n == 1:
        return 1
    f = n*fac(n-1)
    print("ans for", n, "is", f)
    return f

fac(n)
