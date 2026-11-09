from collections import Counter
from roster_calc import get_team_overall, get_all_teams_overall

def get_user_team_rank_and_ovr(user_team, team_lookup):
    """
    Calculates and returns the user team's raw numerical rank and OVR.
    Returns: (rank_int, ovr_int) or (None, None) if team is not found.
    """
    raw_overalls = get_all_teams_overall(team_lookup)
    excluded = {'Free Agents', 'AFC', 'NFC'}
    filtered_overalls = {k: v for k, v in raw_overalls.items() if k not in excluded}
    
    # Safety check if team isn't found
    if user_team not in filtered_overalls:
        return None, None

    # Sort teams descending by OVR rating
    sorted_teams = sorted(filtered_overalls.items(), key=lambda item: item[1], reverse=True)

    current_rank = 1
    for i, (team, ovr) in enumerate(sorted_teams):
        # Update standard competition ranking rules (ties share the same top index)
        if i > 0 and ovr < sorted_teams[i - 1][1]:
            current_rank = i + 1

        # Return integers as soon as your team matches
        if team == user_team:
            return int(current_rank), int(ovr)

    return None, None