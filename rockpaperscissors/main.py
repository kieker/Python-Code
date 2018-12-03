import random

print("Made by John-Henry Ross")
win = "You win"
lose = "Computer wins"
draw = "It was a draw"
life = 5
computer_life = 7
score = 0
drew = 0
choices = ("ROCK", "PAPER", "SCISSORS")
commands = ("HELP", "LIVES", "EXIT")


def win_round(life_now, score_now):
    life_now += 1
    score_now += 1
    print("You win this round")
    return life_now, score_now


def lose_round(life_now):
    life_now -= 1
    print("The computer wins this round")
    return int(life_now)


def draw_round(drew_now):
    drew_now += 1
    print("It was a draw")
    return int(drew_now)


def game_logic(life):
    # Logic

    if ask.upper() == "ROCK":
        computer_choice = random.choices()
        if computer_choice == "SCISSORS":
            win_round(life, score)
        elif computer_choice == "PAPER":
            life = lose_round(life)
        else:
            drew = draw_round(drew)

    if ask.upper() == "SCISSORS":
        computer_choice = random.choices()
        if computer_choice == "PAPER":
            win_round(life, score)
        elif computer_choice == "ROCK":
            life = lose_round(life)
        else:
            drew = draw_round(drew)

    if ask.upper() == "PAPER":
        computer_choice = random.choices()
        if computer_choice == "ROCK":
            win_round(life, score)
        elif computer_choice == "SCISSORS":
            life = lose_round(life)
        else:
            drew = draw_round(drew)

def print_logo():
    logo_file = open("logo.txt", "r")
    for line_logo in logo_file:
        print(line_logo)


while True:
    print("To begin, please fill in the below information")
    username = input("Username:  ")
    password = input("Password:  ")
    search_file = open("accounts.txt", "r")
    found = None

    while not found:
        for line in search_file:
            if username and password in line:
                print("Access granted")
                found = True

            else:
                print("Your username and password was not found. please try again")
                username = input("Username:  ")
                password = input("Password:  ")
                found = False



    ask = input("Which do you choose? : ")

    while ask.upper() not in choices or commands:
        ask = input("Invalid Choice. Please try again, for getting help, type 'help' : ")



    if ask.upper() == "LIVES":
        print("The amount of lives is : " + str(life))
        print("Your Score is : " + str(score))

    if ask.upper() == 'EXIT' or life == 0:
        print("Thank you for playing. Your Score is : " + str(score))
        exit(1)
