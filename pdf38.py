def bool(list):
    i=0
    j=1
    while i<len(list):
        if list[i]%list[j]==0:
            print("True")
            j=j+1
        else:
            print("False")
        i=i+1
        break
bool((-12, 2, -6))