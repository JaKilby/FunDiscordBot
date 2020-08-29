import constants

class TicTacToe(object):
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player_tiles = {self.player1: constants.PLAYER1_TILE,
                             self.player2: constants.PLAYER2_TILE}
        self.board = [[constants.EMPTY_TILE, constants.EMPTY_TILE, constants.EMPTY_TILE],
                      [constants.EMPTY_TILE, constants.EMPTY_TILE, constants.EMPTY_TILE],
                      [constants.EMPTY_TILE, constants.EMPTY_TILE, constants.EMPTY_TILE]]

    def __str__(self):
        row_1 = constants.ROW.format(self.board[0][0], self.board[0][1], self.board[0][2])
        row_2 = constants.ROW.format(self.board[1][0], self.board[1][1], self.board[1][2])
        row_3 = constants.ROW.format(self.board[2][0], self.board[2][1], self.board[2][2])
        return row_1 + constants.ROW_SEPERATOR + row_2 + constants.ROW_SEPERATOR + row_3

    def board_string(self):
        return self.__str__()

    def make_move(self, player, move):
        tile = self.player_tiles[player]
        move = constants.MOVE_DICT[move]
        self.board[move[0]][move[1]] = tile
        win_condition = self.check_win()
        if win_condition[0]:
            return win_condition[1]
        else:
            return self.board_string()

    def validate_move(self, move_string):
        return move_string in constants.MOVE_DICT



    def check_win(self):
        for i in range(2):
            if all(tile == constants.PLAYER1_TILE for tile in self.board[i]):
                return True, "{} wins".format(self.player1)
            elif all(tile == constants.PLAYER2_TILE for tile in self.board[i]):
                return True, "{} wins".format(self.player2)
        for column in zip(*self.board):
            if all(tile == constants.PLAYER1_TILE for tile in column):
                return True, "{} wins".format(self.player1)
            elif all(tile == constants.PLAYER2_TILE for tile in column):
                return True, "{} wins".format(self.player2)
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != constants.EMPTY_TILE:
            if self.board[0][0] == constants.PLAYER1_TILE:
                return True, "{} wins".format(self.player1)
            else:
                return True, "{} wins".format(self.player2)
        elif self.board[2][0] == self.board[1][1] == self.board[0][2] != constants.EMPTY_TILE:
            if self.board[0][0] == constants.PLAYER1_TILE:
                return True, "{} wins".format(self.player1)
            else:
                return True, "{} wins".format(self.player2)
        else:
            return False, ""