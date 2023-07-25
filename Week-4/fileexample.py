import json


def getting_age():
    try:
        return int(input("Please enter your age : "))
    except:
        return False


people = {}
id = 0
while True:
    one_person = {}
    one_person['name'] = input("Please enter your name : ")

    while getting_age() == False :
        one_person['name'] = getting_age()

    one_person['country'] = input("Please enter your country : ")
    id += 1
    people[id] = one_person
    if input("Do you want to continue? ").lower() != 'y':
        break

print(f'You are going to be writing this\n\n{people.__str__()}')

with open('./files/people.json', 'a') as filehandler:

    filehandler.write(json.dumps(people))
