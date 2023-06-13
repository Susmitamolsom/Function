def function(string):
    i=0
    count=0
    count1=0
    while i<len(string):
        if string[i].isupper():
            count=count+1
        elif string[i].islower():
            count1=count1+1
        i=i+1
    return count,count1
print(function('The quick Brow Fox'))