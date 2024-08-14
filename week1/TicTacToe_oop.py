class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("---------")

    def check_winner(self, player):
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
               all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2-i] == player for i in range(3)):
            return True
        return False

    def is_full(self):
        return all(cell != " " for row in self.board for cell in row)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            return True
        return False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def play_game(self):
        while True:
            self.print_board()
            row = int(input(f"Player {self.current_player}, enter row (0-2): "))
            col = int(input(f"Player {self.current_player}, enter column (0-2): "))

            if self.make_move(row, col):
                if self.check_winner(self.current_player):
                    self.print_board()
                    print(f"Player {self.current_player} wins!")
                    break
                elif self.is_full():
                    self.print_board()
                    print("It's a tie!")
                    break
                self.switch_player()
            else:
                print("That cell is already occupied. Try again.")

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()