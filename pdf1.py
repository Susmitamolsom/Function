def my_func(list):
    i=0
    c=0
    b=-1
    while i<len(list):
        if list[i]==list[b]:
            c=c+1
            b=b-1
        i=i+1
    return c
print(my_func(['abc', 'xyz', 'aba', '1221']))