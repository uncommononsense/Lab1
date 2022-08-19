s = str(input("enter word: "))
l = len(s)
p = l-1
t = ""

def IsPali(p, t):

    if p >= 0:

        t = t + s[p]
        return IsPali(p-1, t)
    
    else:
        if t == s:
            print("True")
            return True
        else:
            print("False")
            
IsPali(p, t)
        


    
    
    
