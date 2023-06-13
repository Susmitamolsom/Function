def my_list(num):
    a=str(num)
    i=0
    while i<len(a):
        if a[i]!="0":
            n=a[i]
        i=i+1
        print(n,end="")
my_list(1450)