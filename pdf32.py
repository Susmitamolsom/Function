def func(a):
    i=0
    k=[]
    while i<=a:
        p=i**2
        k.append(p)
        i=i+1
    return k
a=int(input("enter"))
print(func(a))