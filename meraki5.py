def check_numbers(a,b):
    if a%2==0 and b%2==0:
        return "both are even"
    else:
        return "both are odd"
a=int(input("enter 1st no"))
b=int(input("enter 2nd no"))
print(check_numbers(a,b))