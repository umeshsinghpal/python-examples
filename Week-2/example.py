person_age = {}

# input("Do you want to continue? ").lower() !="n"

def check_age(name,age):
    maturity = ""
    if age < 11:
        maturity = "child"
    elif age < 18:
        maturity = "teenager"
    elif age < 65:
        maturity = "adult"
    else:
        maturity = "senior citizen"

    return f'{name} is {maturity}'

while True:

    my_name = input("Enter your name : ")
    my_age = int(input("Enter your age : "))

    person_age[my_name] = my_age

    # if my_age > 18:
    #     if my_age > 65:
    #         print("You are a senior citizen")
    #     else:
    #         print("You are an adult")
    # else:
    #     if my_age < 11:
    #         print("You are a child")
    #     else:
    #         print("You are a teenager")


    for person in person_age:
        if person == my_name:
            print(check_age(person,person_age[person]))

    # for person in person_age:
    #     if person_age[person] < 11:
    #         if person == my_name:
    #             print(f'{person} is a child')
    #         else:
    #             continue
    #     elif person_age[person] < 18:
    #         if person == my_name:
    #             print(f'{person} is a teenager')
    #         else:
    #             continue
    #     elif person_age[person] < 65:
    #         if person == my_name:
    #             print(f'{person} is an adult')
    #         else:
    #             continue
    #     else:
    #         if person == my_name:
    #             print(f'{person} is a senior citizen')
    #         else:
    #             continue


