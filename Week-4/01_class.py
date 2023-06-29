class person:
    name = "shivam"
    occupation = "developer"
    def info(self):
        print("the name of the person is ", self.name)
        print("the occupation of the person is ", self.occupation)
        
objA1 = person()
objA1.name = "rudra"
objA1.occupation = "DB administrator"
objA1.info()
objB1 = person()
objB1.info()