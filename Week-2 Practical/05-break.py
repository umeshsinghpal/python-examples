while input("Do you want to continue (y/n) ").lower()!="n":
    my_age = int(input("Enter your age:"))
    if my_age < 11:
       print("you are a child")
    elif my_age < 18:
       print("you are a teenager")
       break
    elif my_age < 65:
       print("you are an adult")
    else:
       print("you are a senior citizen")