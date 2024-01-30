import logo 
import random
print(logo.logo)
print("Welcome To The Number Guessing Game!")
print("I'm thinking of a number between 1 to 100.")

computer_guess = random.randint(1,100)
# choose difficulty level

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

def diff_level(difficulty_level):
    
    # chances assigned based on difficulty_level.
    if difficulty_level == "easy":
        chance = 10
    elif difficulty_level == "hard":
        chance = 5
    else:
        print("Unauthorized input.")
        return
    
    # check guess is right or not. 
    for counting in range(chance):
        user_guess=(int(input("Make a guess: ")))
        print(f"You have {chance-counting} chances remaining to guess the number.")
        if user_guess == computer_guess:
            print("You guessed it right.")
            return
        elif user_guess > computer_guess:
            print("Too High")
        else:
            print("Too low")
    
# print(computer_guess)
diff_level(difficulty_level=difficulty_level)
