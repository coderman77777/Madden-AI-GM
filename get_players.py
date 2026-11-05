import csv
# get all players for a team.
# optional sorting
# if no team_id specified list all players and no sorting
    # team_id specified and no sorting

def get_players(team_id : int | None = None) -> list:
    with open(r'C:\Users\coderman\Desktop\Developer\Madden-AI-GM\data\test\PLAY.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        players = []
        for row in reader:
            if team_id is None:
                players.append(row)
            elif int(row['TGID']) == team_id:
                players.append(row)
    return players