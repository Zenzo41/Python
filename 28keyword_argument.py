def user(first_name,last_name):
    print(f'Hi {first_name} {last_name}.')
    
    
user("Zen","Sama") #positional argument ie entered values as per the function parameters
user(last_name="Sama",first_name="Zen")

#cost(total=50,shipping=5,discount=0.2) for better readability
user("Zen",last_name="Sama")#keyword_argument always placed after positional argument
#user(first_name="Zen","Sama") Not supported