def func(a,b,c):
    if a>b and a>c:
        return a," is maximum "
    elif b>c and b>a:
        return b,"is maximum "
    else:
        return c,"is maximum"
a=int(input("enter 1st no"))
b=int(input("enter 2nd no"))
c=int(input("enter 3rd no"))
print(func(a,b,c))