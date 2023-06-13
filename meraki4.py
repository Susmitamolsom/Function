# def my_list(list,list1):
#     i=0
#     while i<len(list):
#         sum=list[i]+list1[i]
#         i=i+1
#         print(sum) 
# list=[50, 60, 10]
# list1=[10, 20, 13]
# my_list( list,list1)

# def my_list(list,list1):
#     i=0
#     while i<len(list):
#         if list[i]%2==0 and list1[i]%2==0:
#             print(list[i],list1[i],"both are even")
#         else:
#             print(list[i],list1[i],"both are odd")
#         i=i+1
# list=[2, 6, 18, 10, 3, 75] 
# list1=[6, 19, 24, 12, 3, 87]
# my_list(list,list1)

def my_list(multiple):
    i=0
    k=[]
    while i<len(multiple):
        b=multiple[i]
        j=0
        while j<len(multiple):      
            a=b*multiple[i][j]
            j=j+1
        i=i+1
        k.append(a)
    return k
multiple=[5, 10, 50, 20], [2, 20, 3, 5]
my_list(multiple)