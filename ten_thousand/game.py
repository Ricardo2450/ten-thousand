from ten_thousand.game_logic import GameLogic


def welcome():
    """
    Display welocme message and ask if they like to play
    """
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    choice = input("> ")
    if choice == "y":
        return play(0, 1)
    else:
        print("OK. Maybe another time")



def quit_game():
    quit()




def play(score, round):

    while True:

        print(f"starting round {round}")
        print("Rolling 6 dice")
        num_dice = 6
        return_value = GameLogic.roll_dice(num_dice)
        print(return_value)
        print("Enter dice to keep, or (q)uit:")
        choice = input("> ")
        if choice == "q":
            print(f"Thanks for playing. You earned {score} points")
            quit_game()

        dice_score = GameLogic.calculate_score(choice)
        num_dice = num_dice - len(choice)
        print(f"You have {dice_score} unbanked points and {num_dice} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        choice1 = input("> ")

        if choice1 == "r":
            GameLogic.roll_dice(num_dice) - num_dice
        if choice1 == "b":
            score += dice_score
            print(f"You banked {dice_score} in round {round}")
            print(f"Total score is {score} points")
            round += 1
            play(score, round)
        if choice1 == "q":
            quit_game()












welcome()