from utils.sigmoid import sigmoid
from roster_calc import get_team_overall, get_all_teams_overall, positional_breakdown, get_positional_group, player_value_score

def create_strategy(urgency: int, rank: int, ovr: int, team_id: int, players_by_team: dict):
    if urgency == 70 and sigmoid(rank) > .50:
        
        print("URGENCY LOW")
        roster = positional_breakdown(players_by_team[team_id])

        for position, players in roster.items():
            print(f"\nEvaluating {position} room")
            for player in players:
                overall = player['POVR']
                age = player['PAGE']
                first_name = player['PFNA']
                last_name = player['PLNA']
                score = player_value_score(int(overall), int(age))
                print(f"{first_name} {last_name} {age}yrs {overall}ovr value: {score}")

        # # Check QB OVR
        # qbs = get_positional_group('QB', positional_breakdown(players_by_team[team_id]))
        # print('Evaluating QB Room...')
        # for qb in qbs or []:
        #     overall = qb['POVR']
        #     age = qb['PAGE']
        #     first_name = qb['PFNA']
        #     last_name = qb['PLNA']
        #     print(f"{first_name} {last_name} {age}yrs {overall}ovr value: {player_value_score(int(overall), int(age))}")

    
