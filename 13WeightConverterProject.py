weight = input("Enter your weight: ")
measurement = input(f'(L)bs or (K)gs:')

if(measurement =='P' or measurement =='p'):
    weight_pounds = int(weight) / 0.45
    print("You are "+str(weight_pounds)+ " pounds")
elif(measurement =='K' or measurement =='k'):
    weight_kgs = int(weight) * 0.45
    print("You are "+str(weight_kgs)+ " kgs")
else:
    print("Wrong input : Enter either p for 'pound' or k for 'kgs'")