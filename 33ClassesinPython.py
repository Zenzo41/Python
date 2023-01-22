#Pascal naming EmailClient

#class
class Point:
    #methods
    def move(self):  
        print("Move")
        
    def draw(self):
        print("Draw")
        
        
#using classes
Point1 = Point()
Point1.draw()

Point1.x  = 10
Point1.y = 20
print(Point1.x)

point2 = Point()
point2.move()