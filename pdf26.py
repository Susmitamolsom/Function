def func(a):
    i=1
    while i<=a:
        if i%3==0 and i%5==0:
            print("FIZZBUZZ")
        elif i%3==0:
            print("FIZZ")
        elif i%5==0:
            print("BUZZ")
        i=i+1
a=int(input("enter"))
func(a)