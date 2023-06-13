def my_function(string):
    i=-1
    j=-len(string)
    str=" "
    while i>=j:
        b=string[i]
        i=i-1
        str=str+b
    return str
print(my_function("1234abcd"))