import csv
from pathlib import Path

def load_players(path: Path)-> list[dict]:
    with open(path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

# def group_by_team(players: list[dict])-> dict[int, list[dict]]:
#     team_players = []
#     for player in players:
#         if player['TGID'] == dict
