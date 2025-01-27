#region imports
from Dice import rollFairDie, rollUnFairDie, rollDice
# $JES MISSING CODE #done?
#endregion

#region functions
def main():  # main function to roll nDice fair dice nRolls times and output probabilities
    """
    This function rolls nDice nRolls times and calculates the probabilities for
    each possible score based on P(7)=nTally/nRolls, where nTally is number times I roll a 7, for example.
    :return: nothing
    """
    nDice = 5 # $JES MISSING CODE  # number of dice #done
    nMinScore = nDice # $JES MISSING CODE  # total score if each die scores 1 #done
    nMaxScore = nDice * 6 # $JES MISSING CODE  # total score if each die scores 6 #done
    nNumScores = nMaxScore - nMinScore + 1# $JES MISSING CODE  # number of possible scores #done
    nTally = [0] * nNumScores # $JES MISSING CODE  # create a list with (nMaxScore-nMinScore+1) elements/items #done
    nRolls = 1000# $JES MISSING CODE  # how many times to roll the dice #done
    for i in range(nRolls):  # each loop rolls dice and increments a score #done
        score = rollDice(N=nDice) # $JES MISSING CODE  # call with N=nDice
        nTally[score - nMinScore] += 1 # $JES MISSING CODE  # increment score-nMinScore item b/c 0 indexing start #done
    print("Probabilites for rolling {} dice {} times:".format(nDice, nRolls)) #copilot
    for i in range(nNumScores):  # print the fraction of rolls for each score
        print("Probability of rolling a {}: {:.3f}".format(i + nMinScore, nTally[i] / nRolls)) #copilot

def main2():  # main function to roll nDice unfair dice nRolls times and output probabilities
    """
    This function rolls nDice nRolls times and calculates the probabilities for
    each possible score based on P(7)=nTally/nRolls, where nTally is number times I roll a 7, for example.
    :return: nothing
    """
    nDice = 5# $JES MISSING CODE  # number of dice
    nMinScore = nDice# $JES MISSING CODE  # total score if each die scores 1
    nMaxScore = nDice * 6# $JES MISSING CODE  # total score if each die scores 6
    nNumScores = nMaxScore - nMinScore +1 # $JES MISSING CODE  # number of possible scores
    nTally = [0] * nNumScores # $JES MISSING CODE  # create a list with (nMaxScore-nMinScore+1) elements/items
    nRolls = 1000# $JES MISSING CODE  # how many times to roll the dice
    for i in range(nRolls):  # each loop rolls dice and increments a score
        score = sum(rollUnFairDie() for i in range(nDice)) # $JES MISSING CODE # call with N=nDice #done #copilot
        nTally[score - nMinScore] += 1 # $JES MISSING CODE # increment score-nMinScore item b/c 0 indexing start
    print("After {} rolls of {} dice...".format(nRolls, nDice))
    for i in range(nNumScores):  # print the fraction of rolls for each score
        print("Probability of rolling a {}: {:.3f}".format(i + nMinScore, nTally[i] / nRolls))# $JES MISSING CODE
#endregion

#this if statement prevents these calls if this file is imported as a module.
if __name__ == "__main__":
    main()
    main2()