import random
import string

class BoggleBoard:

  def __init__(self):
    # self.new_board= [["____"],["____"],["____"],["____"]]
    self.board= [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]

  def shake(self):
    for i in range (0,4):
      for n in range (0,4):
        self.board[i][n]= random.choice(string.ascii_letters)
    for list in self.board:
      print(list)

#random letter generator
#random.choice(string.ascii_letters)
hotdog= BoggleBoard()
#print(hotdog.shake())

print("""
              ____
              ____
              ____
              ____
              
              """)
print("1.shake 2.quit")
boggling = False
while boggling == False:
  user_input = input("input a number for the command you wish to execute :>): ")
  if user_input == "1":
    hotdog.shake()
  elif user_input == "2":
    boggling=True
  else:
    print('invalid input my friend')
