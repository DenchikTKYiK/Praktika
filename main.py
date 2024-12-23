def display_board(board):
    print("  0 1 2")
    for i, row in enumerate(board):
        print(i, ' '.join(row))


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    return all(cell != '-' for row in board for cell in row)

def tic_tac_toe():

    board = [['-' for _ in range(3)] for _ in range(3)]
    players = ['x', 'o']
    current_player = 0

    print("Добро пожаловать в одну из самых детских игр <крестики-нолики>, вспомни с первого по 4 класс со своим кентом по парте и выбирай правильную сторону, сторону крестиков или сторону ноликов. Да прибудет с вами гордость и победа, гооооооооооооойда!!!")
    display_board(board)

    while True:
        print(f"Ход игрока {players[current_player]}:")
        try:
            row = int(input("Введите номер строки (0, 1, 2): "))
            col = int(input("Введите номер столбца (0, 1, 2): "))

            if board[row][col] != '-':
                print("Эта клетка уже занята. Выбери другое поле.")
                continue

            board[row][col] = players[current_player]
            display_board(board)

            if check_winner(board, players[current_player]):
                print(f"Игрок победил, гоооооойда!!!!!!!! {players[current_player]} !")
                break

            if is_draw(board):
                print("Ничья!")
                break

            current_player = 1 - current_player

        except (ValueError, IndexError):
            print("ты по-моему перепутал, у нас от 0 и до 2 столбцов, так же со строками, так что поменяй свой выбор воин")


if __name__ == '__main__':
