class A:
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")
        
class B:
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")
class C(A,B):
    def __init__(self):
        print("you are in c class")
        
objC=C()
objC.feature3()
objC.feature4()
objC.feature1()

objA=A()
objA.feature2()