from load import load_players, group_by_team
path = r'C:\Users\coderman\Desktop\Developer\Madden-AI-GM\data\test\PLAY.csv'
print(load_players(path))
grouped = group_by_team(load_players(path))
print(len(grouped[11]))