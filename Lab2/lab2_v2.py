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
        self.current_player = PLAYER_X
        self.player_piece = player_piece
        self.ai_piece = PLAYER_O if player_piece == PLAYER_X else PLAYER_X

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
        print('-' * (COLS * 2 - 1))
        print(' '.join(str(i) for i in range(COLS)))

    # Implement any additional functions needed here
    
    def drop_piece(self, board, col, piece):
        for row in reversed(range(ROWS)):
            if board[row][col] == EMPTY:
                board[row][col] = piece
                return True
        return False

    def get_valid_columns(self):
        return [col for col in range(COLS) if self.board[0][col] == EMPTY]

    def winning_move(self, board, piece):
        # Check all directions
        for r in range(ROWS):
            for c in range(COLS):
                # Horizontal (right)
                if c + 3 < COLS and all(board[r][c + i] == piece for i in range(4)):
                    return True
                # Vertical (down)
                if r + 3 < ROWS and all(board[r + i][c] == piece for i in range(4)):
                    return True
                # Diagonal (down-right)
                if r + 3 < ROWS and c + 3 < COLS and all(board[r + i][c + i] == piece for i in range(4)):
                    return True
                # Diagonal (down-left)
                if r + 3 < ROWS and c - 3 >= 0 and all(board[r + i][c - i] == piece for i in range(4)):
                    return True
        return False

    def evaluate_window(self, window, piece):
        """
        Evaluation of given window. Helper function to evaluate the separate parts of the board called windows

        Parameters:
        - window: list containing values of evaluated window
        - piece: PLAYER_X or PLAYER_O depending on which player's position we evaluate

        Returns:
        - score of the window

        """
        maxCount = 0
        count = 0
        for i in range(4):
            if window[i] == piece or window[i] == None:
                count += 1
            else:
                if count > maxCount:
                    maxCount = count
                count = 0
        return maxCount

    def evaluate_position(self, board, piece):
        """
        Evaluation of position
        Parameters:
        - board: 2d matrix representing evaluated state of the board
        - piece: PLAYER_X or PLAYER_O depending on which player's position we evaluate

        Returns:
        - score of the position

        """
        # Calculate horizontal locations
        max_score = 0
        for r in range(ROWS):
            for c in range(COLS - 3):
                if board[r][c] == piece:
                    temp_score = 0
                    for i in range(4):
                        if board[r][c + i] == piece:
                            temp_score += 1
                        elif board[r][c + i] == None:    
                            temp_score += 1
                            break
                        else:
                            break
                    if temp_score > max_score:
                        max_score = temp_score

        # Calculate vertical locations
        for r in range(ROWS - 3):
            for c in range(COLS):
                if board[r][c] == piece:
                    temp_score = 0
                    for i in range(4):
                        if board[r + i][c] == piece:
                            temp_score += 1
                        elif board[r + i][c] == None:    
                            temp_score += 1
                            break
                        else:
                            break
                    if temp_score > max_score:
                        max_score = temp_score

        # Calculate positively sloped diagonals
        for r in range(ROWS - 3):
            for c in range(COLS - 3):
                if board[r][c] == piece:
                    temp_score = 0
                    for i in range(4):
                        if board[r + i][c + i] == piece:
                            temp_score += 1
                        elif r + i > 0 and board[r + i][c + i] == None and board[r + i - 1][c + i] != None:
                            temp_score += 1
                            break
                        else:
                            break
                    if temp_score > max_score:
                        max_score = temp_score

        # Calculate negatively sloped diagonals
        for r in range(3, ROWS):
            for c in range(COLS - 3):
                if board[r][c] == piece:
                    temp_score = 0
                    for i in range(4):
                        if board[r - i][c + i] == piece:
                            temp_score += 1
                        elif r - i > 0 and board[r - i][c + i] == None and board[r - i-1][c + i]  != None:
                            temp_score += 1
                            break
                        else:
                            break
                    if temp_score > max_score:
                        max_score = temp_score

        return max_score
    

    
    def minimax(self, board, depth, maximizing_player, alpha, beta):
        """
        Minimax with alpha-beta pruning algorithm

        Parameters:
        - board: 2d matrix representing the state, each cell contains either ' ' (empty cell), 'X' (player1), or 'O' (player2) 
        - depth: depth
        - maximizing_player: boolean which is equal to True when the player tries to maximize the score
        - alpha: alpha variable for pruning
        - beta: beta variable for pruning

        Returns:
        - Best value 
        - Best move found

        """

        #Your code starts here
        valid_columns = self.get_valid_columns()
        is_terminal = self.winning_move(board, PLAYER_X) or self.winning_move(board, PLAYER_O) or len(valid_columns) == 0
        
        if depth == 0 or is_terminal:
            return 0,self.evaluate_position(board, PLAYER_O) - self.evaluate_position(board, PLAYER_X)
        
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
    """
    Main game loop implementation. Player1 should play first with 'X', player2 plays second with 'O'
    """
    player_piece = input("Choose your piece (X or O): ").upper()
    while player_piece not in [PLAYER_X, PLAYER_O]:
        player_piece = input("Invalid choice. Choose X or O: ").upper()
    game = ConnectFour(player_piece)
    #minOrMax = True if game.ai_piece == PLAYER_X else False
    game.print_board()

    while True:
        if(len(game.get_valid_columns())) == 0:
            print("Bruh, draw...")
            break
        if game.current_player == game.player_piece:
            try:
                col = int(input(f"Player {game.current_player}, choose a column (0-{COLS - 1}): "))
            except ValueError:
                print("Invalid input. Please enter a valid column number.")
                continue
        else:
            col, _ = game.minimax(game.board, 4, True, -float('inf'), float('inf'))
            print(f"AI chooses column {col}")
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
