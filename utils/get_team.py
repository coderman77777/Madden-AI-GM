import csv

def get_team( team_id: int)-> int:
    with open(r'C:\Users\coderman\Desktop\Developer\Madden-AI-GM\data\test\team.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if team_id == int(row['TGID']):
                team_name = row['TDNA']
                return team_name
                
# TDNA	TLNA	TSNA	TGID
# Bears	Chicago	CHI	0
# Bengals	Cincinnati	CIN	1
# Bills	Buffalo	BUF	2
# Broncos	Denver	DEN	3
# Browns	Cleveland	CLE	4
# Buccaneers	Tampa Bay	TB	5
# Cardinals	Arizona	ARI	6
# Chargers	San Diego	SD	7
# Chiefs	Kansas City	KC	8
# Colts	Indianapolis	IND	9
# Cowboys	Dallas	DAL	10
# Dolphins	Miami	MIA	11
# Eagles	Philadelphia	PHI	12
# Falcons	Atlanta	ATL	13
# 49ers	San Francisco	SF	14
# Giants	New York	NYG	15
# Jaguars	Jacksonville	JAX	16
# Jets	New York	NYJ	17
# Lions	Detroit	DET	18
# Packers	Green Bay	GB	19
# Panthers	Carolina	CAR	20
# Patriots	New England	NE	21
# Raiders	Oakland	OAK	22
# Rams	St. Louis	STL	23
# Ravens	Baltimore	BAL	24
# Redskins	Washington	WAS	25
# Saints	New Orleans	NO	26
# Seahawks	Seattle	SEA	27
# Steelers	Pittsburgh	PIT	28
# Texans	Houston	HOU	29
# Titans	Tennessee	TEN	31
# Vikings	Minnesota	MIN	30
# Free Agents	Free Agents	FA	1009
# AFC	AFC	AFC	1011
# NFC	NFC	NFC	1010