# Guessing Game:

secret_num = 5
guess_count = 0;
guess_limit = 3

while(guess_count < guess_limit ):
    guessed_value = int(input("Enter your guessed number: "))
    guess_count +=1
    
    if(guessed_value  == secret_num):
        print("You are correct!")
        break
else:
    print("Wrong guess!! Try again. ")    
    