def print_board(board):
    print("\n".join([" ".join(row) for row in board]))

def check_win(board):
    # Check rows, columns and diagonals
    for i in range(3):
        if all([cell == 'X' for cell in board[i]]) or all(board[j][i] == 'X' for j in range(3)):
            return 'X'
        if all([cell == 'O' for cell in board[i]]) or all(board[j][i] == 'O' for j in range(3)):
            return 'O'
    
    if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[1][1]
    
    return None

def tictactoe():
    board = [[' ']*3 for _ in range(3)]
    current_player = 'X'
    
    while True:
        print_board(board)
        print("Player's ", current_player, "turn.")

        while True:
            row = int(input('Enter the row (0-2): '))
            column = int(input('Enter the column (0-2): '))
            
            if board[row][column] == ' ':
                board[row][column] = current_player
                break
            else:
                print("Invalid move, try again.")

        winner = check_win(board)
        if winner:
            print("Player ", winner, " wins!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

tictactoe()