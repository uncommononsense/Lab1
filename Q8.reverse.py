s = str(input("Enter string: "))
l = len(s)
p = l-1
t = ""

def reverse(p, t):

    if p >= 0:
        t = t + s[p]
        return reverse(p-1, t)
    else:
        
        return t

print(reverse(p, t))
