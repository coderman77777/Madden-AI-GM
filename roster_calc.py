import sys
import csv
import math


from utils.get_team import get_team
from get_players import get_players
from simplified_players import simplified_players
from config import team_lookup, MY_TEAM_ID, USER_TEAM
# Average our team's OVR and compare to the rest of the league and do the same for each position

# with open(r'C:\Users\coderman\Desktop\Developer\Madden-AI-GM\data\test\PLAY.csv', mode='r', newline='', encoding='utf-8') as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         # Get all 99s 
#         if int(row['POVR']) == 99:
#             player_first_name = row['PFNA']
#             player_last_name = row['PLNA']
#             player_overall = int(row['POVR'])
#             print(f"{player_first_name} {player_last_name} {player_overall} {get_team(int(row['TGID']))}")

    # COL # 21 'PFNA', 22 'PLNA', 'TGID', 'POVR'

def print_team_roster(team_key, output_file):
    if isinstance(team_key, str) and not team_key.isdigit():
        team_name = team_key.strip().title()
        if "49ers" in team_name or "49ers" in team_key:
            team_name = "49ers"
        team_id = team_lookup.get(team_name)
    else:
            team_id = int(team_key)
            team_name = team_lookup.get(team_id, f"Team ID {team_id}")
    if team_id is None:
        print(f"Could not find team: {team_key}", file=output_file)
        return
    my_players = get_players(team_id)
    simplified = simplified_players(my_players)
    simplified.sort(key=lambda player: player[2], reverse=True)
    print(f"Players for {team_name}", file=output_file)
    for first, last, overall in simplified:
        print(f"{overall} {first} {last}", file=output_file)
    print("-" * 30 , file=output_file)

def get_team_overall(players: list):
    if not players:
        return("ERROR: No players for your team")
    total_ovr_pts = 0
    for player in players:
        total_ovr_pts += int(player[2])
    
    avg_ovr = total_ovr_pts / int(len(players))
    
    return (math.ceil(avg_ovr))

def get_all_teams_overall(team_lookup_dict: dict):
    team_overalls = {}

    for key, val in team_lookup_dict.items():
        if isinstance(key, str):
            team_name = key
            team_id = val

            players = get_players(team_id)
            player_list = simplified_players(players)

            team_ovr = get_team_overall(player_list)

            team_overalls[team_name] = team_ovr
    return team_overalls
        

# roster_calc(simplified_players(get_players(MY_TEAM_ID)))
# with open("roster_output.txt", "w") as f:
#     for key, team_id in team_lookup.items():
#         if isinstance(key,str):
#             print_team_roster(team_id, output_file=f)

