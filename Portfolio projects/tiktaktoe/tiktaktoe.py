print('WELCOME TO TIC TAK TOE GAME!')

board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

def display_board(board):
    for row in board:
        for cell in row:
            print(cell, end=" ")  # Print the cell value
        print()  # Move to the next row

def check_winner(board, symbol):
    # Check rows
    for row in board:
        if all(cell == symbol for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(row[col] == symbol for row in board):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True

    return False

def first_player():
    gaming = input('    Put the X or O anywhere you want: ')
    position_mapping = {
        '1/1': (0, 0),
        '1/2': (0, 1),
        '1/3': (0, 2),
        '2/1': (1, 0),
        '2/2': (1, 1),
        '2/3': (1, 2),
        '3/1': (2, 0),
        '3/2': (2, 1),
        '3/3': (2, 2)
    }

    if gaming in position_mapping:
        row, col = position_mapping[gaming]
        if board[row][col] == '-':
            board[row][col] = 'X'
            display_board(board)
        else:
            print('Position already occupied. Try again.')
            display_board(board)

def second_player():
    gaming = input('Where do you want to put the O? ')
    position_mapping = {
        '1/1': (0, 0),
        '1/2': (0, 1),
        '1/3': (0, 2),
        '2/1': (1, 0),
        '2/2': (1, 1),
        '2/3': (1, 2),
        '3/1': (2, 0),
        '3/2': (2, 1),
        '3/3': (2, 2)
    }

    if gaming in position_mapping:
        row, col = position_mapping[gaming]
        if board[row][col] == '-':
            board[row][col] = 'O'
            display_board(board)
        else:
            print('Position already occupied. Try again.')
            display_board(board)

is_on = True
while is_on:
    first_player()
    if check_winner(board, 'X'):
        print('X wins!')
        break
    second_player()
    if check_winner(board, 'O'):
        print('O wins!')
        break
