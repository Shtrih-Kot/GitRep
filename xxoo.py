def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print("|" + "|".join(row) + "|")
        print("-" * 5)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    for row in board:
        if " " in row:
            return None
    return "Ничья"

def is_valid_move(board, row, col):
    if not (0 <= row < 3 and 0 <= col < 3):
        print("Некорректные координаты. Введите числа от 0 до 2")
        return False
    if board[row][col] != " ":
        print("Эта клетка уже занята.")
        return False
    return True

def play_game():
    board = create_board()
    current_player = "X"
    while True:
        print_board(board)
        try:
            row = int(input(f"Игрок {current_player}, введите номер строки (0-2): "))
            col = int(input(f"Игрок {current_player}, введите номер столбца (0-2): "))
        except ValueError:
            print("Некорректный ввод. Введите целые числа.")
            continue

        if is_valid_move(board, row, col):
            board[row][col] = current_player
            winner = check_winner(board)
            if winner:
                print_board(board)
                if winner == "Ничья":
                    print("Ничья!")
                else:
                    print(f"Победил игрок {winner}!")
                break
            current_player = "O" if current_player == "X" else "X"

play_game()