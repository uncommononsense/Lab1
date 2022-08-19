a= int(input("enter number 1: "))
b= int(input("enter number 2: "))

def HCF(a,b):
    if a>b:
        r = a%b

        if r == 0:
            print(b)
            return b

        HCF(b,r)

    elif b>a:
        r = b%a

        if r == 0:
            print(a)
            return a

        HCF(a,r)

HCF(a,b)

        

    

        
