import random
import os

def print_board():
    os.system('cls||clear')
    print(str(board[7]) + "|" + str(board[8]) + "|" + str(board[9]))
    print("------")
    print(str(board[4]) + "|" + str(board[5]) + "|" + str(board[6]))
    print("------")
    print(str(board[1]) + "|" + str(board[2]) + "|" + str(board[3]))

def marker_input():
        marker = ' '
        while marker != 'X' and marker != 'O':
            marker = input('Игрок 1, выберете X или O: ').upper()
        
        if marker == 'X':
            return ('X','O')
        else:
             return ('O','X')

def place_marker(board, marker, position):
     board[position] = marker

def win_check(board, mark):
     # проверка строк
     if (board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or (board[7] == board[8] == board[9] == mark):
          return True
     # проверка столбцов
     if (board[1] == board[4] == board[7] == mark) or (board[2] == board[5] == board[8] == mark) or (board[3] == board[6] == board[9] == mark):
          return True
     # проверка диагоналей
     if (board[1] == board[5] == board[9] == mark) or (board[3] == board[5] == board[7] == mark):
          return True

def choose_first():
     flip = random.randint(0,1)
     if flip == 0:
          return 'Игрок 1'
     else:
          return 'Игрок 2'
     
def space_check(board, position):
     return board[position] == ' '

def full_board_check(board):
     for i in range(1,10):
          if space_check(board, i):
               return False
          
     return True

def player_choose(board):
     position = 0
     while position not in [i for i in range(1,10)] or not space_check(board, position):
          position = int(input('Укажите поле (1-9): '))
        
     return position

def replay():
     choice = input('Хотите поиграть еще? Введите Yes или No: ')
     return choice == 'Yes' or choice == 'yes'

print('Добро пожаловать в игру крестики-нолики')

while True:
     # Игра

     # Настройка игры

     board = [' ']*10
     player1_marker, player2_marker = marker_input()
     turn = choose_first()
     print(turn + ' ходит первым')
     game_on = True
     while game_on:
          if turn == 'Игрок 1':
               # Ход игрока 1
               print_board()
               print('Игрок 1, Ваш ход')
               position = player_choose(board)
               place_marker(board, player1_marker, position)
               if win_check(board, player1_marker):
                    print_board()
                    print('Игрок 1 выйграл')
                    game_on = False
               else:
                    if full_board_check(board):
                         print_board()
                         print('Ничья')
                         game_on = False
                    else:
                         turn = 'Игрок 2'

          else:
               # Ход игрока 2
               print_board()
               print('Игрок 2, Ваш ход')             
               position = player_choose(board)
               place_marker(board, player2_marker, position)
               if win_check(board, player2_marker):
                    print_board()
                    print('Игрок 2 выйграл')
                    game_on = False
               else:
                    if full_board_check(board):
                         print_board()
                         print('Ничья')
                         game_on = False
                    else:
                         turn = 'Игрок 1'
     if not replay():
          break