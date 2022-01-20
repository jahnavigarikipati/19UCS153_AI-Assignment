import math
import time
from players import Human, RandomComputer, SmartComputer


class TicTacToe():
    def __init__(self):
        self.grid = self.make_grid()
        self.current_winner = None

    @staticmethod
    def make_grid():
        return [' ' for _ in range(9)]

    def print_grid(self):
        for row in [self.grid[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_grid_nums():
        number_grid = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_grid:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.grid[square] == ' ':
            self.grid[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = math.floor(square / 3)
        row = self.grid[row_ind*3:(row_ind+1)*3]
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.grid[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.grid[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.grid[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.grid

    def num_empty_squares(self):
        return self.grid.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.grid) if x == " "]


def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_grid_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_grid()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter 
            letter = 'O' if letter == 'X' else 'X' 

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')



if __name__ == '__main__':
    x_player = SmartComputer('X')
    o_player = Human('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
