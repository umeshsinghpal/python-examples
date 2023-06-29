class car:
    
    def __init__(self,make,model):
       self.make = make
       self.model = model
      
    def info(self):
        print("make of the car " , self.make)
        print("model of the car: " , self.model)
        
objcar=car("breeza",2021)
objcar.info()
objcar=car("nexon",2022)
objcar.info()
