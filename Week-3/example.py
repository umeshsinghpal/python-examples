
'''Final Stage'''


persons = {}
id = 0
person_info = ["name", "age", "city", "country", "nickname"]

def fetch_input(get_val):
    message = f'Please enter your {get_val} :\t'
    return input(message)

def age_state(age):
    if age > 60:
         return "You are a senior citizen."
    elif age >= 18:
         return "You are an adult."
    elif age >= 11:
        return "You are a teenager."
    else:
        return "You are a child."

def response(person, person_info):
    # id = 220
    # print(f'inside function id is {id}')
    try:
        return f'Hello! {person[person_info[0]]}, your nick name is {person[person_info[4]]}, {age_state(int(person[person_info[1]]))} You live in {person[person_info[2]]}, {person[person_info[3]]}.\n'
    except ValueError as valerr:
        print("Please enter an interger for age")
        return f'Hello! {person[person_info[0]]}, your nick name is {person[person_info[4]]}. You live in {person[person_info[2]]}, {person[person_info[3]]}.\n'


while input(f'\n Do you want to continue (y/n) :').lower() == 'y':
    id += 1 
    person = {}
    for info in person_info:
        person[info] = fetch_input(info)
    persons[id] = person
    # print(f'outside function id is {id}')
    print(response(person,person_info))
    # print(f'outside function id is {id}')
  
for person in persons:
    print(response(persons[person],person_info))



'''Third Stage'''

# persons = {}
# person_info = ["name", "age", "city", "country"]
# id = 0

# def fetch_input(get_val):
#     message = f'Please enter your {info} :\t'
#     return input(message)

# def age_state(age):
#     if age > 60:
#         return "You are a senior citizen."
#     elif age >= 18:
#         return "You are an adult."
#     elif age >= 11:
#         return "You are a teenager."
#     else:
#         return "You are a child."

# def response(person, person_info):
#     print(f'Hello! {person[person_info[0]]}, {age_state(int(person_info[1]))} You live in {person[person_info[2]]}, {person[person_info[3]]}.\n')



# while input(f'\n Do you want to continue (y/n) :').lower() == 'y':
#     person = {}
#     id += 1
#     for info in person_info:
#         person[info] = 

#     persons[id] = person

# for person in persons:




'''Second Stage'''

# persons = {}
# person_info = ["name", "age", "city", "country"]
# id = 0

# while input(f'\n Do you want to continue (y/n) :').lower() == 'y':
#     person = {}
#     id += 1
#     for info in person_info:
#         message = f'Please enter your {info} :\t'
#         person[info] = input(message)
#     if int(person[person_info[1]]) > 60:
#         age_message = "You are a senior citizen."
#     elif int(person[person_info[1]]) >= 18:
#         age_message = "You are an adult."
#     elif int(person[person_info[1]]) >= 11:
#         age_message = "You are a teenager."
#     else:
#         age_message = "You are a child."
#     print(f'Hello! {person[person_info[0]]}, {age_message} You live in {person[person_info[2]]}, {person[person_info[3]]}.\n')
#     persons[id] = person

# for person in persons:
#     if int(persons[person][person_info[1]]) > 60:
#         age_message = "You are a senior citizen."
#     elif int(persons[person][person_info[1]]) >= 18:
#         age_message = "You are an adult."
#     elif int(persons[person][person_info[1]]) >= 11:
#         age_message = "You are a teenager."
#     else:
#         age_message = "You are a child."
#     print(f'Hello! {persons[person][person_info[0]]}, {age_message} You live in {persons[person][person_info[2]]}, {persons[person][person_info[3]]}.\n')


'''First Stage'''

# person_info = ["name", "age", "city", "country"]

# person = {}

# for info in person_info:
#     message = f'Please enter your {info} :\t'
#     person[info] = input(message)

# if int(person[person_info[1]]) > 60:
#     age_message = "You are a senior citizen."
# elif int(person[person_info[1]]) >= 18:
#     age_message = "You are an adult."
# elif int(person[person_info[1]]) >= 11:
#     age_message = "You are a teenager."
# else:
#     age_message = "You are a child."

# print(f'Hello! {person[person_info[0]]}, {age_message} You live in {person[person_info[2]]}, {person[person_info[3]]}.\n')


























