from IPython.display import clear_output
import random

# display the current board, argument is a list
def display_board(board):
    clear_output()
    print(' '*8 + '|'+' '*8 + '|'+' '*8)
    print(f'{board[1]:^8}|{board[2]:^8}|{board[3]:^8}')
    print(' '*8 + '|' + ' '*8 + '|' + ' '*8)
    print('-'*8 + '|' + '-'*8 + '|' + '-'*8)
    print(' '*8 + '|'+' '*8 + '|'+' '*8)
    print(f'{board[4]:^8}|{board[5]:^8}|{board[6]:^8}')
    print(' '*8 + '|' + ' '*8 + '|' + ' '*8)
    print('-'*8 + '|' + '-'*8 + '|' + '-'*8)
    print(' '*8 + '|'+' '*8 + '|'+' '*8)
    print(f'{board[7]:^8}|{board[8]:^8}|{board[9]:^8}')
    print(' '*8 + '|' + ' '*8 + '|' + ' '*8)
 
 # define the player markers, ask for user input to select
 def player_input():
    p1 = ''
    while p1!='x' and p1!='o':
        p1 = input('Player 1: do you want to be X or O?').lower()
    if p1 == 'x':
        p1 = 'X'
        p2 = 'O'
    else:
        p1 = 'O'
        p2 = 'X'
    return p1,p2

# place a marker at a given index in the board list
def place_marker(board,marker,position):
    board[position] = marker

# check the winning scenarios
def win_check(board,mark):
    return ((board[1]==mark and board[2]==mark and board[3]==mark) or 
    (board[4]==mark and board[5]==mark and board[6]==mark) or
    (board[7]==mark and board[8]==mark and board[9]==mark) or
    (board[1]==mark and board[4]==mark and board[7]==mark) or
    (board[2]==mark and board[5]==mark and board[8]==mark) or
    (board[3]==mark and board[6]==mark and board[9]==mark) or
    (board[1]==mark and board[5]==mark and board[9]==mark) or
    (board[3]==mark and board[5]==mark and board[7]==mark))

# randomly select who goes first
def choose_first():
    num = random.randint(1,2)
    print(f'Player {num} will go first')
    return num

# chcek if an index position in the board list is available
def space_check(board,position):
    return board[position]==' '

# check whether the board list is fully populated
def full_board_check(board):
    return ' ' not in board

# get player input for their next position, to be used as index pos
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose your next position\n'))
    return position

# play again
def replay():
    return input('Do you want to play again?\n')[0].lower()=='y'

# game logic
# print board with position numbers
print('Welcome to Naughts and Crosses!')
number_board = ['#','1','2','3','4','5','6','7','8','9']
print('Board numbers are as shown\n')
print(' '*8 + '|'+' '*8 + '|'+' '*8)
print(f'{number_board[1]:^8}|{number_board[2]:^8}|{number_board[3]:^8}')
print(' '*8 + '|' + ' '*8 + '|' + ' '*8)
print('-'*8 + '|' + '-'*8 + '|' + '-'*8)
print(' '*8 + '|'+' '*8 + '|'+' '*8)
print(f'{number_board[4]:^8}|{number_board[5]:^8}|{number_board[6]:^8}')
print(' '*8 + '|' + ' '*8 + '|' + ' '*8)
print('-'*8 + '|' + '-'*8 + '|' + '-'*8)
print(' '*8 + '|'+' '*8 + '|'+' '*8)
print(f'{number_board[7]:^8}|{number_board[8]:^8}|{number_board[9]:^8}')
print(' '*8 + '|' + ' '*8 + '|' + ' '*8)

while True:
    # Set the initial game
    game_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    if input('Are you ready to play? Yes or No')[0].lower()=='y':
        game_on = True
    else:
        game_on = False
    display_board(game_board)

    while game_on:
        #Player 1 Turn
        if turn == 1:
            position = player_choice(game_board)
            place_marker(game_board, player1_marker, position)
            if win_check(game_board, player1_marker):
                display_board(game_board)
                print('Player 1 wins the game!')
                break
            elif full_board_check(game_board):
                display_board(game_board)
                print('It is a draw!')
                break
            else:
                display_board(game_board)
                turn = 2
        # Player2's turn.
        else:
            position = player_choice(game_board)
            place_marker(game_board, player2_marker, position)
            if win_check(game_board, player2_marker):
                display_board(game_board)
                print('Player 2 wins the game!')
                break
            elif full_board_check(game_board):
                display_board(game_board)
                print('It is a draw!')
                break
            else:
                display_board(game_board)
                turn = 1
    if not replay():
        break
