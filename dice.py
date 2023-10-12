from random import choice


class Dice:
    allDice = []

    def __init__(self, dieLtr):
        self.dieLtr = list(dieLtr)
        self.add_qu()
        Dice.allDice.append(self)

    def __str__(self):
        return f"{self.dieLtr}"

    def random_letter(self):
        return choice(self.dieLtr)

    @classmethod
    def make_all_dice(self, allDiceLetters):
        for dice in allDiceLetters:
            Dice(dice)
            # print(dice)

    def add_qu(self):
        for die in range(len(self.dieLtr)):
            if self.dieLtr[die] == "Q":
                self.dieLtr[die] += "u"


if __name__ == "__main__":
    die1 = Dice("ABDQEF")
    print(die1)
