from tic_tac_toe.playing_symbol import PlayingSymbol


def get_opponent_symbol(player_symbol: PlayingSymbol) -> PlayingSymbol:
    """Gets opponent symbol based on player's symbol.

    Parameters
    ----------
    player_symbol : PlayingSymbol
        Symbol of a player

    Returns
    -------
    PlayingSymbol
        Symbol of opponent
    """
    if player_symbol == PlayingSymbol.CROSS:
        return PlayingSymbol.CIRCLE
    elif player_symbol == PlayingSymbol.CIRCLE:
        return PlayingSymbol.CROSS
