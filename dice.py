from random import choice

class Dice:

    allDice = []

    def __init__(self, dieLtr):
        self.dieLtr = dieLtr
        Dice.allDice.append(self)

    def random_letter(self):
        return choice(list(self.dieLtr))

    @classmethod
    def make_all_dice(self, allDiceLetters):
        for dice in allDiceLetters:
            Dice(dice)
            print(dice)



if __name__ == "__main__":
    die1 = Dice("ABCDEF")
    print(Dice.allDice)
    # print(die1.random_letter())
    # print(Dice.allDice)
    Dice.make_all_dice(["AAEEGN", "ELRTTY","AOOTTW","ABBJOO","EHRTVW","CIMOTU","DISTTY","EIOSST","DELRVY","ACHOPS","HIMNQU","EEINSU","EEGHNW","AFFKPS","HLNNRZ","DEILRX"])
    print(len(Dice.allDice))
#     for die in Dice.allDice:
#         print(die.random_letter())