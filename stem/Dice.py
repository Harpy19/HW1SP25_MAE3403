# region imports
from Die import rollFairDie, rollUnFairDie #JES MISSING CODE #done
# endregion
# region functions
def rollDice(N=1):
    total_score = 0
    for i in range(N):
        total_score += rollFairDie()
        return total_score
    """
    This function simulates rolling N dice simultaneously by using a loop that rolls
    a single die N times and totaling the score.
    :param N: the number of dice to be rolled
    :return: the total score from rolling N dice
    """
    #JES MISSING CODE
    pass

def rollUnFairDice(N=1):
    """
    This function simulates rolling N, UnFair dice simultaneously by using a loop that rolls
    a single die N times and totals the score.
    :param N: the number of dice to be rolled
    :return: the total score from rolling N dice
    """
    #JES MISSING CODE
    pass

# endregion