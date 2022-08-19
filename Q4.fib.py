n = int(input("enter number: "))

def fib(n):
    if n == 1:
        return 0
    if n ==2:
        return 1
    else:
        d = fib(n-1) + fib (n-2)
    return d

print(fib(n))
