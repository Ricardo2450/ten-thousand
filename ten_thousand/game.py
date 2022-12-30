from ten_thousand.game_logic import GameLogic


class Game:

    def __init__(self):

        self.round = 1
        self.num_dice = 6
        self.total_score = 0
        self.dice_score = 0

    def welcome(self):
        """
        Display welocme message and ask if they like to play
        """
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        choice = input("> ")
        if choice == "y":
            return self.play(0, 1, 6)
        else:
            print("OK. Maybe another time")



    def quit_game(self):
        quit()

    #def end_round(self, rounds, banked_points):
        #print(f"You banked {banked_points} in round {rounds}")
        #print(f"Total score is {self.dice_score} points")


    def play(self,total_score, round, num_dice):

        print(f"starting round {round}")

        while True:

            print(f"Rolling {self.num_dice} dice")
            GameLogic.roll_dice(self.num_dice)
            print(GameLogic.roll_dice(self.num_dice))
            print("Enter dice to keep, or (q)uit:")
            choice = input("> ")
            if choice == "q":
                print(f"Thanks for playing. You earned {self.total_score} points")
                self.quit_game()

            # self.dice_score += GameLogic.calculate_score(choice)
            # self.num_dice = self.num_dice - len(choice)
            # print(f"You have {self.dice_score} unbanked points and {self.num_dice} dice remaining")
            print("(r)oll again, (b)ank your points or (q)uit:")
            choice1 = input(">>> ")



            # self.rolled = GameLogic.roll_dice
            # rolled_dice = self.rolled(self.num_dice)
            print("this is the return value", choice)
            # points_scored = 0
            # points_scored = GameLogic.calculate_score(choice)
            # validate_score = points_scored
            # print("this is the VS", validate_score)
            # if validate_score == 0:
            print("this is GL", GameLogic.calculate_score(choice))
            print("this is GL type", type(GameLogic.calculate_score(choice)))

            
            if GameLogic.calculate_score(choice) == 0:
                print("Zilch!!! Round over")
                # self.end_round(rounds, 0)
                print(f"You banked {self.dice_score} in round {round}")
                print(f"Total score is {self.total_score} points")
                round += 1
                self.num_dice = 6
                self.dice_score = 0
                self.play(total_score, round, num_dice)


            elif choice1 == "r":
                if self.num_dice == 0:
                    self.num_dice = 6
                continue



            elif choice1 == "b":
                self.total_score += self.dice_score
                print(f"You banked {self.dice_score} in round {round}")
                print(f"Total score is {self.total_score} points")
                round += 1
                self.num_dice = 6
                self.dice_score = 0
                self.play(total_score, round, num_dice)

            elif choice1 == "q":
                self.quit_game()

            else:
                self.dice_score += GameLogic.calculate_score(choice)
                self.num_dice = self.num_dice - len(choice)
                print(f"You have {self.dice_score} unbanked points and {self.num_dice} dice remaining")










test_game = Game()
test_game.welcome()