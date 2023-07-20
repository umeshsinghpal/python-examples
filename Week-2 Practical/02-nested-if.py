my_age = int(input("Enter your age:"))
if my_age > 18:
    if my_age > 65:
        print("you are a senior citizen")
    else:
        print("You are an adult")
else:
    if my_age < 11:
        print("you are a child")
    else:
        print("you are a teenager")
    