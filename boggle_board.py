from random import shuffle
from dice import Dice

class BoggleBoard:
  
  def __init__(self):
    self.board = [["","","",""],["","","",""],["","","",""],["","","",""]]
    Dice.make_all_dice(["AAEEGN", "ELRTTY","AOOTTW","ABBJOO","EHRTVW","CIMOTU","DISTTY","EIOSST","DELRVY","ACHOPS","HIMNQU","EEINSU","EEGHNW","AFFKPS","HLNNRZ","DEILRX"])


  def __str__(self):
    return f'{self.board}'

  def shake(self):
    # upperCase = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    shuffle(Dice.allDice)
    counter = 0
    for row in range(4):
      for cell in range(4):
        self.board[row][cell] = Dice.allDice[counter].random_letter()
        counter +=1
        # cell = choice(upperCase)

  def print_board(self):
    for row in range(4):
      for cell in range(4):
        if self.board[row][cell] == "":
          print("_",end="")
        else:
          print(self.board[row][cell], end="")
      print()






boggle = BoggleBoard()
boggle.shake()
boggle.print_board()
print(' ')
boggle.shake()
boggle.print_board()