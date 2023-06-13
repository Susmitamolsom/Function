# def func(n):
#     n=int(input("enter"))
#     for i in range(2,n):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)           
# func(())

def func(n):
    i=2
    while i<=n:
        j=2
        while j<=i:
            if i%j==0:
                break
            else:
                print(i)
            j=j+1
        i=i+1
n=int(input("enter number"))
func(n)