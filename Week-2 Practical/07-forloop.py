person_age = {}
while input("Do yo want to continue (y/n)").lower()!='n':
     my_name = input("Enter Your name :")
     my_age = int(input("Enter your age:"))
     person_age[my_name] = my_age
     for person in person_age:
        if person_age[person] < 11:
            if person ==  my_name:
               print(f'{person} is a child')
            else:
               continue
        elif person_age[person] < 18:
           if person ==  my_name:
              print(f'{person} is a teenager')
           else:
             continue
        elif person_age[person] < 65:
           if person == my_name:
              print(f'{person} is an adult') 
           else:
             continue
        else:
           if person == my_name:
              print(f'{person} is a senior citizen')
           else:
             continue
           

