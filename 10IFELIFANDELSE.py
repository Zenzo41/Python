# Simulation One
is_hot =True
is_cold = False 
if is_hot:
    print("Drink a lot of water")
elif is_cold:
    print("Wear warm clothes")
    
else:
    print("Enjoy your day")
    
# Simulation Two
good_credit = True
price = 1000000

if good_credit:
   downpayment = 0.10 * price
else:
    downpayment = 0.20 * price
    
print(f"Down payment: {downpayment}")