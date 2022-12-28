from random import randint
from collections import Counter


class GameLogic:

    @staticmethod
    def roll_dice(num_dice):
        values = []
        for i in range(num_dice):
            value = randint(1, 6)
            values.append(value)

        return tuple(values)


    def calculate_score(values):
        score = 0
        counts = Counter(values)
        pair_counter = 0

        for die in counts:
            #counts[die] = counts.get(die, 0) + 1
            if counts[die] == 2:
                pair_counter += 1
            if pair_counter < 3 and len(counts) < 6:
                if die == 1:
                    if counts[die] == 1:
                        score += 100
                    elif counts[die] == 2:
                        score += 200
                    elif counts[die] == 3:
                        score += 1000
                    elif counts[die] == 4:
                        score += 2000
                    elif counts[die] == 5:
                        score += 3000
                    elif counts[die] == 6:
                        score += 4000
                if die == 2:
                    if counts[die] == 1:
                        score += 0
                    elif counts[die] == 2:
                        score += 0
                    elif counts[die] == 3:
                        score += 200
                    elif counts[die] == 4:
                        score += 400
                    elif counts[die] == 5:
                        score += 600
                    elif counts[die] == 6:
                        score += 800
                if die == 3:
                    if counts[die] == 1:
                        score += 0
                    elif counts[die] == 2:
                        score += 0
                    elif counts[die] == 3:
                        score += 300
                    elif counts[die] == 4:
                        score += 600
                    elif counts[die] == 5:
                        score += 900
                    elif counts[die] == 6:
                        score += 1200
                if die == 4:
                    if counts[die] == 1:
                        score += 0
                    elif counts[die] == 2:
                        score += 0
                    elif counts[die] == 3:
                        score += 400
                    elif counts[die] == 4:
                        score += 800
                    elif counts[die] == 5:
                        score += 1200
                    elif counts[die] == 6:
                        score += 1600
                if die == 5:
                    if counts[die] == 1:
                        score += 50
                    elif counts[die] == 2:
                        score += 100
                    elif counts[die] == 3:
                        score += 500
                    elif counts[die] == 4:
                        score += 1000
                    elif counts[die] == 5:
                        score += 1500
                    elif counts[die] == 6:
                        score += 2000
                if die == 6:
                    if counts[die] == 1:
                        score += 0
                    elif counts[die] == 2:
                        score += 0
                    elif counts[die] == 3:
                        score += 600
                    elif counts[die] == 4:
                        score += 1200
                    elif counts[die] == 5:
                        score += 1800
                    elif counts[die] == 6:
                        score += 2400
        if pair_counter == 1 and counts[die] == 3:
            score = 1500
        if pair_counter == 3:
            score = 1500
        if len(counts) == 6:
            score = 1500
        return score
