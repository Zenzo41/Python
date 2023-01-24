import random

class Dice:
    def Roll(self):
        val1 = random.randint(1,6)
        val2 = random.randint(1,6)
        return val1,val2  #got confused at first attempt
        
        
        
d1 = Dice()
print(d1.Roll())