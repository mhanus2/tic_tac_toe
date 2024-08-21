from tic_tac_toe.game import Game
from tic_tac_toe.playing_symbol import PlayingSymbol

play = True

print('Welcome to Tic-Tac-Toe!\n')
while play:
    playing_symbol = input('Please choose a symbol: X or O\nYour choice: ').upper()
    if playing_symbol not in ['X', 'O']:
        print('You can only choose either X or O!')
        continue
    playing_symbol = PlayingSymbol(playing_symbol)
    game = Game(playing_symbol)
    game.show_board()
    game.play()

    next_game = None
    while next_game not in ['Y', 'N']:
        next_game = input('Do you want another game? Please enter Y or N\n').upper()
        if next_game not in ['Y', 'N']:
            print('Please enter only Y or N!')
        elif next_game == 'Y':
            continue
        else:
            play = False
