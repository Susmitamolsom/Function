def bool(list):
    i=0
    sum=0
    while i<len(list):
        if list[i]==True:
            sum=sum+1
        i=i+1
    return sum
print(bool([True, True, True, False,
True, True, True, True ,
True, False, True, False,
True, False, False, True ,
True, True, True, True ,
False, False, True, True]))