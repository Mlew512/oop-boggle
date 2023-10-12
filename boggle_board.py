import random
import string


class BoggleBoard:
    def __init__(self):
        # self.new_board= [["____"],["____"],["____"],["____"]]
        self.board = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
        self.dice = [
            ["A", "A", "E", "E", "G", "N"],
            ["E", "L", "R", "T", "T", "Y"],
            ["A", "O", "O", "T", "T", "W"],
            ["A", "B", "B", "J", "O", "O"],
            ["E", "H", "R", "T", "V", "W"],
            ["C", "I", "M", "O", "T", "U"],
            ["D", "I", "S", "T", "T", "Y"],
            ["E", "I", "O", "S", "S", "T"],
            ["D", "E", "L", "R", "V", "Y"],
            ["A", "C", "H", "O", "P", "S"],
            ["H", "I", "M", "N", "Qu", "U"],
            ["E", "E", "I", "N", "S", "U"],
            ["E", "E", "G", "H", "N", "W"],
            ["A", "F", "F", "K", "P", "S"],
            ["H", "L", "N", "N", "R", "Z"],
            ["D", "E", "I", "L", "R", "X"],
        ]

    def shake(self):
        for i in range(0, 4):
            for n in range(0, 4):
                self.board[i][n] = random.choice(self.dice[random.randint(0, 15)])
                if self.board[i][n] != "Qu":
                  self.board[i][n] += " "
        for list in self.board:
            print(" ".join(list))


# random letter generator
# random.choice(string.ascii_letters)
hotdog = BoggleBoard()
# print(hotdog.shake())

print(
    """
____
____
____
____

              """
)
print("1.shake 2.quit")
boggling = False
while boggling == False:
    user_input = input("input a number for the command you wish to execute :>): ")
    if user_input == "1":
        hotdog.shake()
    elif user_input == "2":
        boggling = True
    else:
        print("invalid input my friend")
