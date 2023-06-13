def func(list):
    i=0
    sum=0
    while i<len(list):
        sum=sum+list[i]
        i=i+1
    return sum
print(func((8, 2, 3, 0, 7)))