from utils.sigmoid import sigmoid


def create_strategy(urgency: int, rank: int, ovr: int):
    if urgency == 70 and sigmoid(rank) > .50:
    
        print("URGENCY LOW")
    
