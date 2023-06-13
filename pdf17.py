def vote(age):
    if age>=18:
        return "eligible to vote"
    else:
        return "not eligible to vote"
age=int(input("enter"))
print(vote(age))