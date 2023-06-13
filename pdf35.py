def list(age):
    if age<=13:
        return "Drink Toddy"
    elif age<=17:
        return "Drink coke"
    elif age<=20:
        return "Drink beer "
    elif age<=30:
        return "Drink whiskey"
age=int(input("enter age"))
print(list(age))