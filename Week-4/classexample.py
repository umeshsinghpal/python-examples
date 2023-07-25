import json

class person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def get_age_status(self):
        if self.get_age() > 60:
            return "senior citizen"
        elif self.get_age() >= 18:
            return "adult"
        elif self.get_age() >= 11:
            return "teenager"
        else:
            return "child"

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def set_age(self,age):
        self.__age = age

    def get_age(self):
        return int(self.__age)

    def get_person(self):
        return f'Hello! {self.get_name().capitalize()}. You are as of now {self.get_age_status()}'
    
class citizen(person):
    def __init__(self, name, age, country):
        super().__init__(name, age)
        self.__country = country

    def set_country(self,country):
        self.__country = country

    def get_country(self):
        return self.__country

    def get_citizen_status(self):
        if self.get_age() >= 18:
            return f"You are a citizen of {self.get_country().capitalize()} and can now pay taxes."
        else:
            return f"You are a citizen of {self.get_country().capitalize()} but we will have to wait till we can get taxes out of you."

    def get_person(self):
        return f'{super().get_person()}. {self.get_citizen_status()}'
    

# id = 0
# people = {}

# while True:
#     name = input("Please enter your name : ")
#     age = input("Please enter your age : ")
#     country = input("Please enter your country : ")
#     people[id] = citizen(name, age, country)
#     id += 1
#     if input("Do you want to continue? ").lower() != 'y':
#         break

# for one in people:
#     print(people[one].get_person())



with open('./files/people.json', 'r') as filehandler:
    jsoncontent = json.loads(filehandler.read())
    for content in jsoncontent:
        one = citizen(jsoncontent[content]['name'],jsoncontent[content]['age'],jsoncontent[content]['country'])
        print(one.get_person())
