def even(nums):
    i=0
    while i<=nums:
        if i%2==0:
            print(i,"even") 
        else:
            print(i,"odd")
        i=i+1
nums=int(input("enter"))
even(nums)