
# def func(list):
#     i=0
#     max=0
#     while i<len(list):
#         if list[i]>max:
#             max=list[i]
#         i=i+1
#     return max
# print(func([4,6,2,1,9,63,-134,566]))

def func(list):
    i=0
    j=1
    min=0
    while i<len(list):
        if list[i]<list[j]:
            min=list[i]
            j=j+1
        i=i+1
    return min
print(func([-52, 56, 30, 29, -54, 0, -110]))