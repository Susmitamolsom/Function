def my_function():
    i=1
    k=[]
    while i<=30:
        b=i**2
        i=i+1
        k.append(b)
        if i==6:
           break
    return k
print(my_function())