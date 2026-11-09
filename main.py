import sys
from collections import Counter
from utils.get_team import get_team
from get_players import get_players
from simplified_players import simplified_players
from config import team_lookup, MY_TEAM_ID, USER_TEAM, URGENCY
from roster_calc import get_team_overall, get_all_teams_overall
from urgency import get_urgency
from decisions import create_strategy
from rank import get_user_team_rank_and_ovr
def main():
    print("ARLO Model v0.0.1")
    print("*+*+*")
    print(f"Team: {USER_TEAM}")
    print(f"Team ID: {MY_TEAM_ID}")
    print("Team OVR: " + str(get_team_overall(simplified_players(get_players(MY_TEAM_ID)))))
    rank, ovr = get_user_team_rank_and_ovr(USER_TEAM, team_lookup)
    print(f"Urgency: {get_urgency(URGENCY)}")
    raw_overalls = get_all_teams_overall(team_lookup)
    excluded = {'Free Agents', 'AFC', 'NFC'}
    filtered_overalls = {k: v for k, v in raw_overalls.items() if k not in excluded}
    ovr_counts = Counter(filtered_overalls.values())
    sorted_teams = sorted(filtered_overalls.items(), key=lambda item: item[1], reverse=True)
    COLOR_GREEN = "\033[92m"
    COLOR_YELLOW = "\033[93m"
    COLOR_RED = "\033[91m"
    COLOR_RESET = "\033[0m"
    current_rank = 1
    for i, (team, ovr) in enumerate(sorted_teams):
        if i > 0 and ovr < sorted_teams[i- 1][1]:
            current_rank = i + 1

        is_tied = ovr_counts[ovr] > 1
        rank_str = f"T={current_rank}" if is_tied else f"{current_rank}"

        if not is_tied:
            if current_rank % 10 == 1 and current_rank % 100 !=11: suffix = "st"
            elif current_rank % 10 == 2 and current_rank % 100 !=12: suffix = "nd"
            elif current_rank  %10 == 3 and current_rank % 100 != 13: suffix = "rd"
            else: suffix = "th"
            rank_str += suffix
        else:
            base_rank = current_rank
            if base_rank % 10 == 1 and base_rank % 100 != 11: suffix = "st"
            elif current_rank % 10 == 2 and current_rank % 100 !=12: suffix = "nd"
            elif current_rank  %10 == 3 and current_rank % 100 != 13: suffix = "rd"
            else: suffix = "th"
            rank_str += suffix

        if team == USER_TEAM:
            if current_rank <= 5:
                color = COLOR_GREEN
            elif current_rank <= 15:
                color = COLOR_YELLOW
            else:
                color = COLOR_RED

            print(f"{color}--> {rank_str} | {team}: {ovr}{COLOR_RESET}")
        else:
            print(f"{rank_str} | {team}: {ovr}")
        # print(create_strategy(URGENCY, rank, ovr))
if __name__ == "__main__":
    main()