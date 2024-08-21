import random
import time

from tic_tac_toe.playing_symbol import PlayingSymbol
from tic_tac_toe.utils import get_opponent_symbol


class Game:
    def __init__(self, playing_symbol: PlayingSymbol):
        self._active = True
        self._player_symbol = playing_symbol
        self._opponent_symbol = get_opponent_symbol(playing_symbol)
        self._empty_symbol = '   '
        self._board = {
            'A': {
                '1': self._empty_symbol,
                '2': self._empty_symbol,
                '3': self._empty_symbol
            },
            'B': {
                '1': self._empty_symbol,
                '2': self._empty_symbol,
                '3': self._empty_symbol
            },
            'C': {
                '1': self._empty_symbol,
                '2': self._empty_symbol,
                '3': self._empty_symbol
            }
        }

    @property
    def _available_locations(self) -> list[str]:
        """Available locations.

        Returns
        -------
        list[str]
            All available locations
        """
        empty_locations = []
        for column, rows in self._board.items():
            for row, symbol in rows.items():
                if symbol == self._empty_symbol:
                    empty_locations.append(column + row)
        return empty_locations

    def play(self) -> None:
        """Main loop of game."""
        while self._active:
            if self._available_locations:
                location = input(
                    f'Please choose a location where you want to add your symbol: {", ".join(self._available_locations)}\nYour choice: ').upper()
                if location not in self._available_locations:
                    print('\nThis location is either full or not on board!')
                    continue
                self._board[location[0]][location[1]] = f' {self._player_symbol.value} '

                self.show_board()

                if self._is_player_winner():
                    print('Player won!\n')
                    self._active = False
                    continue

                print('Opponent is thinking...\n')
                time.sleep(2)

                opponent_choice = random.choice(self._available_locations)
                self._board[opponent_choice[0]][opponent_choice[1]] = f' {self._opponent_symbol.value} '
                print(f'Oponnent chose {opponent_choice}!\n')

                self.show_board()

                if self._is_opponent_winner():
                    print('Opponent won!\n')
                    self._active = False
            else:
                print('Game over. Noone wins!')
                self._active = False

    def show_board(self) -> None:
        """Shows playing board."""
        print()
        print(self._empty_symbol + self._empty_symbol.join(['1', '2', '3']))
        for column, rows in self._board.items():
            print(f'{column} ' + '|'.join(rows.values()))
            if column != 'C':
                print('  -----------')
        print()

    def _is_player_winner(self) -> bool:
        """Checks if player is a winner.

        Returns
        -------
        bool
            True if player is a winner, False otherwise.
        """
        return self._check_winner(self._player_symbol)

    def _is_opponent_winner(self) -> bool:
        """Checks if opponent is a winner.

        Returns
        -------
        bool
            True if opponent is a winner, False otherwise.
        """
        return self._check_winner(self._opponent_symbol)

    def _check_winner(self, symbol: PlayingSymbol) -> bool:
        """Checks if given symbol is winner.

        Parameters
        ----------
        symbol : PlayingSymbol
            Symbol to be checked

        Returns
        -------
        bool
            True if symbol is winner, False otherwise
        """
        symbol = f' {symbol.value} '
        # Check rows
        for row in self._board:
            if self._board[row]['1'] == self._board[row]['2'] == self._board[row]['3'] == symbol:
                return True

        # Check columns
        for col in ['1', '2', '3']:
            if self._board['A'][col] == self._board['B'][col] == self._board['C'][col] == symbol:
                return True

        # Check diagonals
        if self._board['A']['1'] == self._board['B']['2'] == self._board['C']['3'] == symbol:
            return True
        if self._board['A']['3'] == self._board['B']['2'] == self._board['C']['1'] == symbol:
            return True

        return False
