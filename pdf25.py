def func(list):
    i=0
    n=0
    p=0
    while i<len(list):
        if list[i]<0:
            n=n+1
        else:
            p=p+1
        i=i+1
    return("negative =",n,"positive=",p)
print(func([2,-7,5,-64,-14]))