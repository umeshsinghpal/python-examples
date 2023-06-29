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
    def drive(self):    
        print("you are driving bmw, enjoy") 
objcar=car() 
objcar.drive()
objcar.stop()

objbmw=BMW() 
objbmw.drive()  
objbmw.stop()