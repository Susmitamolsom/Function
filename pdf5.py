def my_function(List):
    i=0
    k=[]
    while i<len(List):
        if List[i] not in k:
            k.append(List[i])
        i=i+1
    return k
print(my_function([1,2,3,3,3,3,4,5]))