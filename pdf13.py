def even(a):
    if a%2==0:
        return a,"is even"
    else:
        return a,"is odd"
a=int(input("enter"))
print(even(a))