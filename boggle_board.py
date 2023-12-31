from random import shuffle
from dice import Dice


class BoggleBoard:
    def __init__(self):
        self.board = [
            ["", "", "", ""],
            ["", "", "", ""],
            ["", "", "", ""],
            ["", "", "", ""],
        ]
        Dice.make_all_dice(
            [
                "AAEEGN",
                "ELRTTY",
                "AOOTTW",
                "ABBJOO",
                "EHRTVW",
                "CIMOTU",
                "DISTTY",
                "EIOSST",
                "DELRVY",
                "ACHOPS",
                "HIMNQU",
                "EEINSU",
                "EEGHNW",
                "AFFKPS",
                "HLNNRZ",
                "DEILRX",
            ]
        )
        self._score = 0

    def __str__(self):
        return f"{self.board}"

    def shake(self):
        shuffle(Dice.allDice)
        counter = 0
        for row in range(4):
            for cell in range(4):
                self.board[row][cell] = Dice.allDice[counter].random_letter()
                counter += 1
        self.print_board()

    def print_board(self):
        for row in range(4):
            for cell in range(4):
                if self.board[row][cell] == "":
                    print("__", end="")
                else:
                    if len(self.board[row][cell]) == 2:
                        print(f"{self.board[row][cell]} ", end="")
                    else:
                        print(f"{self.board[row][cell]}  ", end="")
            print()

    def include_word(self, word: str):
        word = word.upper()
        if self.check_rows(word) or self.check_cols(word) or self.check_diagnols(word):
            return True
        return False

    def check_rows(self, word: str):
        for row in self.board:
            row_word = "".join(row)
            reversed_word = row_word[::-1]
        if row_word == word or reversed_word == word:
            return True
        return False

    def check_diagnols(self, word: str):
        diagnol1 = "".join([self.board[i][i] for i in range(4)])
        reversed_diangol1 = diagnol1[::-1]
        diagnol2 = "".join([self.board[i - 1][-i] for i in range(1, 5)])
        reversed_diangol2 = diagnol2[::-1]
        if word == diagnol1 or word == reversed_diangol1:
            return True
        if word == diagnol2 or word == reversed_diangol2:
            return True
        return False

    def check_cols(self, word: str):
        for j in range(4):
            col_word = ""
            for i in range(4):
                col_word += self.board[i][j]
            reversed_word = col_word[::-1]
            if reversed_word == word or col_word == word:
                return True
        return False

    @staticmethod
    def check_all_words():
        with open("words.txt") as file:
            data = file.read()
            data = data.split("\n")
        word_not_found = True
        iterations = 0
        while word_not_found:
            iterations += 1
            boggle.shake()
            for word in data:
                if boggle.include_word(word):
                    print(word)
                    word_not_found = False
            if word_not_found:
                print("No words here")
        print(f"It took {iterations} iterations to find a word")

    def play(self):
        self.shake()
        while True:
            answer = input("Type in word or 'q' to quit: ")
            if answer == "q":
                break
            if self.include_word(answer):
                self._score += 1
                print(f"{answer} is on the board")
            else:
                print("That's not there")
        print(f"You scored: {self._score}")


if __name__ == "__main__":
    boggle = BoggleBoard()
    boggle.play()
    print()
    BoggleBoard.check_all_words()
