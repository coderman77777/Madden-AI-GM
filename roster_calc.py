import math
from collections import defaultdict
from simplified_players import simplified_players
from config import team_lookup, AGE_BEST, AGE_WORST, OVERALL_BEST
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

def print_team_roster(team_key, players_by_team, output_file):
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
    my_players = players_by_team[team_id]
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

def get_all_teams_overall(players_by_team: dict[int, list[dict]], team_lookup: dict)-> dict[str,int]:
    team_overalls = {}

    for key, val in team_lookup.items():
        if isinstance(key, str):
            team_name = key
            team_id = val

            players = players_by_team[team_id]
            player_list = simplified_players(players)

            team_ovr = get_team_overall(player_list)

            team_overalls[team_name] = team_ovr
    return team_overalls
        

# roster_calc(simplified_players(get_players(MY_TEAM_ID)))
# with open("roster_output.txt", "w") as f:
#     for key, team_id in team_lookup.items():
#         if isinstance(key,str):
#             print_team_roster(team_id, output_file=f)


# QB - most important
# Position Key
# 0 - QB
# 1 - RB
# 2 - FB
# 3 - WR
# 4 - TE
# 5 - LT
# 6 - LG
# 7 - C
# 8 - RG
# 9 - RT
# 10 - LE
# 11 - RE
# 12 - DT
# 13 - LOLB
# 14 - MLB
# 15 - ROLB
# 16 - CB
# 17 - FS
# 18 - SS 
# 19 - K
# 20 - P

POS_LOOKUP = {
    0: "QB",  1: "HB",  2: "FB",  3: "WR",  4: "TE",
    5: "LT",  6: "LG",  7: "C",   8: "RG",  9: "RT",
    10: "LE", 11: "RE", 12: "DT", 13: "LOLB", 14: "MLB",
    15: "ROLB", 16: "CB", 17: "FS", 18: "SS", 19: "K", 20: "P"
}
def positional_breakdown(roster: dict)-> dict[str, list[dict]]:
    grouped_players = defaultdict(list)

    for player in roster:
        pos_id = int(player['PPOS'])
        pos_name = POS_LOOKUP.get(pos_id, "f{pos_id}")
        grouped_players[pos_name].append(player)

    for pos_name, players in grouped_players.items():
        players.sort(key=lambda p: int(p['POVR']), reverse=True)
        # print(f"\n {pos_name}")
        # print("==========")
        # for p in players:
        #     print(f"{p['PFNA']} {p['PLNA']}: {p['POVR']}")

    return grouped_players


def get_positional_group(position_group: str, grouped_players: dict[str, list[dict]] ) -> dict[str, list[dict]]:
    key = position_group.upper()
    if key not in grouped_players:
        raise ValueError(f"Invalid Position  '{position_group}'. Valid options: {list(grouped_players.keys())}")
    return grouped_players[key]


# calculate positional attributes WHEN LOL?
def player_value_score(ovr: int, age: int, min_age: int = AGE_BEST, max_age: int = AGE_WORST)-> float:
    age_score = max(0.0, min(1.0, (max_age - age) / (max_age - min_age))) ** 2
    
    overall_score = ovr / float(OVERALL_BEST)

    return(0.7 * overall_score) + (0.3 * age_score)




# TODO:
# def score_positional_value() ...


      
    