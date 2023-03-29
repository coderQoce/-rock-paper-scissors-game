import re

while True:
    name = input(" please what is your name: ")
    if re.search(r'\d|\s', name):
        print('Name should not have any number or space')
        continue
    else:
        print("welcome", name, "to the adventure!")

    answer = input(
        "you are walking  toward a t-juntion where would you go right or left: ").lower().strip()

    if answer == "right" or answer == 'r':
        answer = input(
            "As you were going right you came across a river are you going to swim across or walk across? :"
        ).lower().strip()
        if answer == "swim":
            print("you swam and got eaten by a crocodile!")
        elif answer == "walk across":
            print("you walked for too long and got lost.You lose")
        else:
            print('You must choose an option.')

    elif answer == "left" or answer == 'l':
        answer = input(
            "You came to a bridge it not in a good condition you gonna cross or head back (cross/back)? "
        ).lower().strip()
        if answer == "cross":
            input(
                "you crossed the bridge and it collapsed and you fell and Died.Game over!")
        elif answer == "back":
            answer = input(
                "you went and met a group of strangers do you talk to them (yes/no)? ").lower().strip()
            if answer == "yes":
                print(
                    "You talked to them and they helped you to win your adventure.You Win!!")
                break
            elif answer == "no":
                print("The strangers got angry and beat you to death.You lose")
        else:
            print('Try Again')
            continue

    else:
        print('You must choose an option. Try again')
        continue
