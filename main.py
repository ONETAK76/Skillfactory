def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([cell != " " for row in board for cell in row])

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while not check_winner(board, "X") and not check_winner(board, "O") and not is_full(board):
        print_board(board)
        row = int(input(f"Player {current_player}, enter the row (0, 1, 2): "))
        col = int(input(f"Player {current_player}, enter the column (0, 1, 2): "))
        if board[row][col] == " ":
            board[row][col] = current_player
            current_player = "O" if current_player == "X" else "X"
        else:
            print("This cell is already taken!")
    print_board(board)
    if check_winner(board, "X"):
        print("Player X wins!")
    elif check_winner(board, "O"):
        print("Player O wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
