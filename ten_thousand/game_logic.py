# from random import randint
# from collections import Counter
#
#
# class GameLogic:
#
#     @staticmethod
#     def roll_dice(num_dice):
#         values = []
#         for i in range(num_dice):
#             value = randint(1, 6)
#             values.append(value)
#
#         return tuple(values)
#
#
#     def calculate_score(values):
#         score = 0
#         counts = Counter(values)
#         #print(len(counts))
#         pair_counter = 0
#
#         for die in counts:
#             #counts[die] = counts.get(die, 0) + 1
#             if counts[die] == 2:
#                 pair_counter += 1
#             if pair_counter < 3 and len(counts) < 6:
#                 if die == "1":
#                     if counts[die] == 1:
#                         score += 100
#                     elif counts[die] == 2:
#                         score += 200
#                     elif counts[die] == 3:
#                         score += 1000
#                     elif counts[die] == 4:
#                         score += 2000
#                     elif counts[die] == 5:
#                         score += 3000
#                     elif counts[die] == 6:
#                         score += 4000
#                 if die == "2":
#                     if counts[die] == 1:
#                         score += 0
#                     elif counts[die] == 2:
#                         score += 0
#                     elif counts[die] == 3:
#                         score += 200
#                     elif counts[die] == 4:
#                         score += 400
#                     elif counts[die] == 5:
#                         score += 600
#                     elif counts[die] == 6:
#                         score += 800
#                 if die == "3":
#                     if counts[die] == 1:
#                         score += 0
#                     elif counts[die] == 2:
#                         score += 0
#                     elif counts[die] == 3:
#                         score += 300
#                     elif counts[die] == 4:
#                         score += 600
#                     elif counts[die] == 5:
#                         score += 900
#                     elif counts[die] == 6:
#                         score += 1200
#                 if die == "4":
#                     if counts[die] == 1:
#                         score += 0
#                     elif counts[die] == 2:
#                         score += 0
#                     elif counts[die] == 3:
#                         score += 400
#                     elif counts[die] == 4:
#                         score += 800
#                     elif counts[die] == 5:
#                         score += 1200
#                     elif counts[die] == 6:
#                         score += 1600
#                 if die == "5":
#                     if counts[die] == 1:
#                         score += 50
#                     elif counts[die] == 2:
#                         score += 100
#                     elif counts[die] == 3:
#                         score += 500
#                     elif counts[die] == 4:
#                         score += 1000
#                     elif counts[die] == 5:
#                         score += 1500
#                     elif counts[die] == 6:
#                         score += 2000
#                 if die == "6":
#                     if counts[die] == 1:
#                         score += 0
#                     elif counts[die] == 2:
#                         score += 0
#                     elif counts[die] == 3:
#                         score += 600
#                     elif counts[die] == 4:
#                         score += 1200
#                     elif counts[die] == 5:
#                         score += 1800
#                     elif counts[die] == 6:
#                         score += 2400
#         if pair_counter == 1 and counts[die] == 3:
#             score = 1500
#         if pair_counter == 3:
#             score = 1500
#         if len(counts) == 6:
#             score = 1500
#         return score



# dont remove after this


from collections import Counter
from random import randint


class GameLogic:
    @staticmethod
    def roll_dice(num=6):
        # version_1

        return tuple([randint(1, 6) for _ in range(num)])

    @staticmethod
    def calculate_score(dice):
        """
        dice is a tuple of integers that represent the user's selected dice pulled out from current roll
        """
        # version_1

        if len(dice) > 6:
            raise Exception("Cheating Cheater!")

        counts = Counter(dice)

        if len(counts) == 6:
            return 1500

        if len(counts) == 3 and all(val == 2 for val in counts.values()):
            return 1500

        score = 0

        ones_used = fives_used = False

        for num in range(1, 6 + 1):

            pip_count = counts[num]

            if pip_count >= 3:

                if num == 1:

                    ones_used = True

                elif num == 5:

                    fives_used = True

                score += num * 100

                # handle 4,5,6 of a kind
                pips_beyond_3 = pip_count - 3

                score += score * pips_beyond_3

                # bug if 2 threesomes? Let's test it

                # 1s are worth 10x
                if num == 1:
                    score *= 10

        if not ones_used:
            score += counts.get(1, 0) * 100

        if not fives_used:
            score += counts.get(5, 0) * 50

        return score

    @staticmethod
    def validate_keepers(roll, keepers):
        # version_3

        # pro tip: you can do some math operations with counters
        # check https://docs.python.org/3/library/collections.html#collections.Counter
        keeper_counter = Counter(keepers)
        roll_counter = Counter(roll)

        # a "valid" result is an empty Counter result
        result = keeper_counter - roll_counter

        # an empty Counter is falsy, so use "not" to flip it
        return not result

    @staticmethod
    def get_scorers(dice):
        # version_3

        all_dice_score = GameLogic.calculate_score(dice)

        if all_dice_score == 0:
            return tuple()

        scorers = []

        # for i in range(len(dice)):

        for i, val in enumerate(dice):
            sub_roll = dice[:i] + dice[i + 1 :]
            sub_score = GameLogic.calculate_score(sub_roll)

            if sub_score != all_dice_score:
                scorers.append(val)

        return tuple(scorers)