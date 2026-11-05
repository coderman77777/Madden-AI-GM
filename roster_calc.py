import csv

from utils.get_team import get_team
from get_players import get_players
from simplified_players import simplified_players
from config import team_lookup, MY_TEAM_ID
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

def print_team_roster(team_key):
    if isinstance(team_key, str) and not team_key.isdigot():
        team_name = team_key.strip.title()
        if "49ers" in team_name or "49ers" in team_key:
            team_name = "49ers"
        team_id = team_lookup.get(team_name)
    else:
            team_id = int(team_key)
            team_name = team_lookup.get(team_id, f"Team ID {team_id}")
    if team_id is None:
        print(f"Could not find team: {team_key}")
        return
    my_players = get_players(team_id)
    simplified = simplified_players(my_players)
    simplified.sort(key=lambda player: player[2], reverse=True)
    print(f"Players for {team_name}")
    for first, last, overall in simplified:
        print(f"{overall} {first} {last}")

for key, team_id in team_lookup.items():
    if isinstance(key,str):
        print_team_roster(team_id)