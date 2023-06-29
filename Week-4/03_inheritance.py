class car(object):
    def __init__(self):
        print("you just created the car instance")
    def drive(self):
        print("car start")
    def stop(self):
        print("car stopped")
class BMW(car):
    def __init__(self): 
        print("you created the bmw instance ")
objC=car()  
objC.drive()
objC.stop()

objB=BMW() 
objB.drive()
objB.stop()
