import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check if there are any available moves left
def is_moves_left(board):
    for row in board:
        if ' ' in row:
            return True
    return False

# Function to evaluate the board
def evaluate(board):
    # Check rows, columns, and diagonals for a win
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != ' ':
            return 10 if board[row][0] == 'X' else -10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return 10 if board[0][col] == 'X' else -10

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return 10 if board[0][0] == 'X' else -10

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return 10 if board[0][2] == 'X' else -10

    return 0

# Minimax function with Alpha-Beta pruning
def minimax(board, depth, is_max, alpha, beta):
    score = evaluate(board)

    if score == 10 or score == -10:
        return score - depth if score == 10 else score + depth

    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, not is_max, alpha, beta))
                    board[i][j] = ' '
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    else:
        best = math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, not is_max, alpha, beta))
                    board[i][j] = ' '
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

# Function to find the best move for the AI
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = ' '
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

# Main function to play the game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)
        if not is_moves_left(board) or evaluate(board) != 0:
            break

        row, col = map(int, input("Enter your move (row and column): ").split())
        if board[row][col] == ' ':
            board[row][col] = 'O'
        else:
            print("Invalid move. Try again.")
            continue

        if not is_moves_left(board) or evaluate(board) != 0:
            break

        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = 'X'

    print_board(board)
    score = evaluate(board)
    if score == 10:
        print("AI wins!")
    elif score == -10:
        print("You win!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_game()
