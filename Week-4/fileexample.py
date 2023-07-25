import json


people = {}
id = 0
while True:
    one_person = {}
    one_person['name'] = input("Please enter your name : ")
    one_person['age'] = int(input("Please enter your age : "))
    one_person['country'] = input("Please enter your country : ")
    id += 1
    people[id] = one_person
    if input("Do you want to continue? ").lower() != 'y':
        break

print(f'You are going to be writing this\n\n{people.__str__()}')

with open('./files/people.json', 'a') as filehandler:

    filehandler.write(json.dumps(people))
