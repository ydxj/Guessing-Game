from art import logo
import random
gess = random.randint(1,100)
def life_left(lifes):
    if lifes == 'hard':
        return 5
    else :
        return 10
game_over = False
print(gess)
while not game_over:
    print(logo)
    print("Welcome to the Number Guessing Game!")
    ask = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    lifes = life_left(ask)
    gesse = 0
    while gess != gesse and lifes != 0:
        
        print(f"You have {lifes} attempts remaining to guess the number.")
        gesse = int(input("Gess a number : "))
        if gess > gesse:
            print("Too low. \n Guess again.")
            lifes -= 1
        elif gess < gesse:
            print("Too Hight. \n Guess again.")
            lifes -= 1
        elif gess == gesse :
            print(f"You got it! The answer was {gess}.")
    ask = input("Do you want to play it another time? type 'yes' or 'no' : ").lower()
    if ask == 'no':
        game_over = True
    
print("See you soone")