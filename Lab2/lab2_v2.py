import copy
import random

EMPTY = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'
ROWS = 6
COLS = 7


class ConnectFour:
    """
    Class for game Connect 4
    """
    def __init__(self, player_piece):
        self.board = [[EMPTY] * COLS for _ in range(ROWS)]
        self.player_piece = player_piece
        self.ai_piece = PLAYER_O if player_piece == PLAYER_X else PLAYER_X
        self.current_player = PLAYER_X

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
        print('-' * (COLS * 2 - 1))
        print(' '.join(str(i) for i in range(COLS)))

    def drop_piece(self, board, col, piece):
        for row in reversed(range(ROWS)):
            if board[row][col] == EMPTY:
                board[row][col] = piece
                return True
        return False

    def is_valid_location(self, col):
        return self.board[0][col] == EMPTY

    def get_valid_columns(self):
        return [c for c in range(COLS) if self.is_valid_location(c)]

    def winning_move(self, board, piece):
        # Check horizontals
        for r in range(ROWS):
            for c in range(COLS - 3):
                if all(board[r][c + i] == piece for i in range(4)):
                    return True
        # Check vertvals
        for r in range(ROWS - 3):
            for c in range(COLS):
                if all(board[r + i][c] == piece for i in range(4)):
                    return True
        # Check diagonals r->l
        for r in range(ROWS - 3):
            for c in range(COLS - 3):
                if all(board[r + i][c + i] == piece for i in range(4)):
                    return True
        # Check diagonals l->r
        for r in range(3, ROWS):
            for c in range(COLS - 3):
                if all(board[r - i][c + i] == piece for i in range(4)):
                    return True

        return False

    def minimax(self, board, depth, maximizing_player, alpha, beta):
        valid_columns = self.get_valid_columns()
        is_terminal = self.winning_move(board, PLAYER_X) or self.winning_move(board, PLAYER_O) or len(valid_columns) == 0
        
        if depth == 0 or is_terminal:
            if self.winning_move(board, PLAYER_X):
                return (None, 1000000)
            elif self.winning_move(board, PLAYER_O):
                return (None, -1000000)
            else:
                return (None, 0)
        
        if maximizing_player:
            value = -float('inf')
            best_col = random.choice(valid_columns)
            for col in valid_columns:
                temp_board = copy.deepcopy(board)
                self.drop_piece(temp_board, col, self.ai_piece)
                new_score = self.minimax(temp_board, depth - 1, False, alpha, beta)[1]
                if new_score > value:
                    value = new_score
                    best_col = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return best_col, value
        else:
            value = float('inf')
            best_col = random.choice(valid_columns)
            for col in valid_columns:
                temp_board = copy.deepcopy(board)
                self.drop_piece(temp_board, col, self.player_piece)
                new_score = self.minimax(temp_board, depth - 1, True, alpha, beta)[1]
                if new_score < value:
                    value = new_score
                    best_col = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return best_col, value


def main():
    player_piece = input("Choose your piece (X or O): ").upper()
    while player_piece not in [PLAYER_X, PLAYER_O]:
        player_piece = input("Invalid choice. Choose X or O: ").upper()
    
    game = ConnectFour(player_piece)
    game.print_board()
    
    while True:
        if game.current_player == game.player_piece:
            col = int(input(f"Player {game.current_player}, choose a column (0-{COLS - 1}): "))
        else:
            col, _ = game.minimax(game.board, 4, True, -float('inf'), float('inf'))
            print(f"Bot chooses column {col}")
        
        if col in game.get_valid_columns():
            game.drop_piece(game.board, col, game.current_player)
            game.print_board()
            if game.winning_move(game.board, game.current_player):
                print(f"Player {game.current_player} wins!")
                break
            game.current_player = game.ai_piece if game.current_player == game.player_piece else game.player_piece
        else:
            print("Invalid move. Try again.")


if __name__ == "__main__":
    main()
