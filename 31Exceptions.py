try:
    age = int(input("Age:"))
   
    income = 20000
    risk = income/age
   
except ValueError:
    print("You have entered invalid value.")    
except ZeroDivisionError:
    print("Age can not be Zero")