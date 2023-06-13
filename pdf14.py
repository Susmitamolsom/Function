def prime (a):
    i=1
    fact=0
    while i<=a:
        if a%i==0:
            fact=fact+1
        else:
            pass
        i=i+1
    if fact==2:
        return ("prime no")
    else:
        return ("not prime")
a=int(input("enter"))
print(prime(a))