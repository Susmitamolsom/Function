def func(list):
    i=0
    k=[]
    while i<len(list):
        j=0
        sum=0
        b=str(list[i])
        while j<len(b):
            sum=int(b[j])+sum
            j=j+1
        i=i+1
        k.append(sum)
    return k
print(func([12, 67, 98, 34]))