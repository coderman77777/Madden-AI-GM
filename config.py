# AI GM config.py v 0.0.1

MY_TEAM_ID = 11 # THE AI'S TEAM (in our case the Dolphins)
CURRENT_SEASON = 0 # How do we handle being in an offseason on the config?
# Weights

TOTAL_SEASONS_LEFT = 30 - CURRENT_SEASON
#TDNA   #TGID ---- #TEAM.csv
Bears = 0
Bengals = 1
Bills = 2
Broncos = 3
Browns = 4
Buccaneers = 5
Cardinals = 6
Chargers = 7
Chiefs = 8 
Colts = 9
Cowboys = 10
Dolphins = 11
Eagles = 12
Falcons = 13
49ers = 14
Giants = 15
Jaguars = 16
Jets = 17
Lions = 18
Packers = 19
Panthers = 20
Patriots = 21
Raiders = 22
Rams = 23
Ravens = 24
Redskins = 25
Saints = 26
Seahawks = 27
Steelers = 28
Texans = 29
Titans = 31
Vikings = 30
Free Agents = 1009
AFC = 1011
NFC = 1010



# TEAM IDS


# We want the model to always try to aim to win as many Super Bowls as possible
# That being said we should allow the model to devise a multi season strategy to win
# as much in the future
URGENCY = 100 - TOTAL_SEASONS_LEFT
# For now we will leave as this the further from 100 the less urgency


# Total team roster OVR determines strategy
# If it's high maybe add pieces from trading
# If it's low consider drafting and trading players for draft picks.
# Breakdown each position find weak areas
# Compare to other teams
# Find teams with surplus in certain positions