def simplified_players(players_list: list) -> list:
    players = []
    for player in players_list:
        players.append((player['PFNA'],player['PLNA'],player['POVR']))
    return players