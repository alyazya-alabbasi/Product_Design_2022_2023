from random import randint
from colorama import Fore
from colorama import Style


radiant = ['rock','paper','scissors']

# computer choosing
neef = radiant[randint(0,2)]

Yazya = False

while Yazya == False:
# set Yazya to True
    Yazya = input("rock, paper, scissors? ")
    print("neef chose "+neef+" \n")

    if Yazya == neef:
        print("Tie!")
    elif Yazya == "rock":
        if neef == "paper":
            print("You lose!", neef, "covers", Yazya)
        else:
            print("You win!", Yazya, "smashes", neef)
    elif Yazya == "paper":
        if neef == "scissors":
            print("You lose!", neef, "cut", Yazya)
        else:
            print("You win!", Yazya, "covers", neef)
    elif Yazya == "scissors":
        if neef == "rock":
            print("You lose...", neef, "smashes", Yazya)
        else:
            print("You win!", Yazya, "cut", neef)
    else:
        print("That's not a valid play. Check your spelling!")
    #Yazya was set to True, but we want it to be False so the loop continues
    Yazya = False
    neef = radiant[randint(0,2)]
    #where color text
    # print(colored('rock', 'red'), colored('scissors', 'grey'))
    print(f"This is {Fore.CYAN}scissors{Style.RESET_ALL}!")
    print(f"This is {Fore.RED}rock{Style.RESET_ALL}!")