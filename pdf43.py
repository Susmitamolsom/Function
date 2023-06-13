def func(list):
    i=-1
    a=int(input("enter no"))
    while i<len(list):
        p=list[:a:i]
        print(p)
        i=i-1
        break
func(['a', 1, '2', 5, 'b', 'q'])