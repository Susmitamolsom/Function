# def function(numbers):
#     i=0
#     max=0
#     while i<len(numbers):
#         if numbers[i]>max:
#             max=numbers[i]
#         i=i+1
#     return max
# print(function([3, 5, 7, 34, 2, 89, 2, 5]))


# def function(numbers):
#     i=0
#     sum=0
#     while i<len(numbers):
#         sum=sum+numbers[i]
#         i=i+1
#     return sum
# print(function( [1, 2, 3, 4, 5]))


# def function(unorder_list):
#     i=0
#     while i<len(unorder_list):
#         unorder_list.sort()
#         i=i+1
#     return unorder_list
# print(function([6, 8, 4, 3, 9, 56, 0, 34, 7, 15]))


# def function(reverse_list):
#     i=-1
#     k=[]
#     a=-len(reverse_list)
#     while i>=(a):
#         k.append(reverse_list[i])
#         i=i-1
#     return k
# print(function(["Z", "A", "A", "B", "E", "M", "A", "R", "D"]))

def function(list):
    i=0
    j=1
    min=0
    while i<len(list):
        if list[i]<list[j]:
            min=list[i]
            j=j+2
        i=i+1
    return min
print(function([8, 6, 4, 8, 4, 50, 2, 7]))