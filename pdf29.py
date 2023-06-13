def func(a):
    i=1
    while i<=a:
        if i%3==0:
            print(i,end=" ")
        elif i%5==0:
            print(i,end=" ")
        i=i+1
a=int(input("enter"))
func(a)