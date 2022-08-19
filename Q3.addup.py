n = int(input("Enter number: "))

def addup(n):
    if n < 0 or n - int(n) != 0:
        print("enter a valid number")
    if n == 1:+
        return 1
    add = n + addup(n-1)
    print("sum: ", add)
    return add

addup(n)
