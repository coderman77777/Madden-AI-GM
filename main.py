import sys

from utils.get_team import get_team
from get_players import get_players
from simplified_players import simplified_players
from config import team_lookup, MY_TEAM_ID, USER_TEAM
from roster_calc import get_team_overall, get_all_teams_overall

def main():
    print("ARLO Model v0.0.1")
    print("*+*+*")
    print(f"Team: {USER_TEAM}")
    print(f"Team ID: {MY_TEAM_ID}")
    print("Team OVR: " + str(get_team_overall(simplified_players(get_players(MY_TEAM_ID)))))
    raw_overalls = get_all_teams_overall(team_lookup)
    excluded = {'Free Agents', 'AFC', 'NFC'}
    filtered_overalls = {k: v for k, v in raw_overalls.items() if k not in excluded}
    sorted_teams = sorted(filtered_overalls.items(), key=lambda item: item[1], reverse=True)
    for team, ovr in sorted_teams:
        print(f"{team}: {ovr}")
   


if __name__ == "__main__":
    main()