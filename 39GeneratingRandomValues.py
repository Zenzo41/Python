# Using the built in packages and modules

import random

print("# 0 to 1")
for i in range(3):
    print(random.random())
   
print("#10 -> 30")
for i in range(3):
    print(random.randint(10,30))
   
   
print("Choosing the leader")
members = ["John" , "Mary" ,"Zen","Harry"]
leader = random.choice(members)
print(leader)