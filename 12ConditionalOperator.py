# Simulation One
temp = 20
if(temp > 30):
    print("It's a hot day")
elif(temp < 10):
    print("It's a cold day")
else:
    print("It's neither hot nor cold")
    
# Simulation Two
name = input("Enter your name: ")
if(len(name)< 3):
    print("Name must be atleast 3 characters")
elif(len(name)>50):
    print("Name can be max of 50 cahracters")
else:
    print("Name looks good")