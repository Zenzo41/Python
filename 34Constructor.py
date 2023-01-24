class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
        
   
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")
        

point = Point(10,20)
print(point.x)
point.x = 11
print(point.x)

#Function with constructor name and talk() method:

class Person:
    def talk(self):
        print("talk")
        
    def __init__(self,name) :
        self.name = name
        


john = Person("John Smith")
print(john.name)
john.talk()