def my_function(List):
    i=0
    k=[]
    while i<len(List):
        if List[i]%2==0:
            k.append(List[i])
        i=i+1
    return k
print(my_function([1, 2, 3, 4, 5, 6, 7, 8, 9]))