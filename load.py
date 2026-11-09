import csv
from pathlib import Path
from collections import defaultdict

def load_players(path: Path)-> list[dict]:
    with open(path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def group_by_team(players: list[dict])-> dict[int, list[dict]]:
    team_players = defaultdict(list)
    for player in players:
        team_id = int(player["TGID"])
        team_players[team_id].append(player)
    return team_players