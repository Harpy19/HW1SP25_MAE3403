# region imports
from Die import rollFairDie as rfd

#JES MISSING CODE (done?)
# endregion
# region function declarations
def main():
    """
    This function rolls a fair die 1000 times and tallies the number of 1's, 2's etc.  Finally,
    it calculates and outputs the probability of each possible score.
    :return: nothing
    """
    scores = [0] * 6 #JES MISSING CODE  # create a list with 6 elements/items initialized to 0's (done) (from google)
    n = 1000 #JES MISSING CODE  # how many times to roll the die (done)
    for i in range(n):  # each time through the loop, roll die and increment a score
        score = rfd()  # score = 1 to 6  #changed to "rdf()"
        scores[score - 1] += 1  # increment score-1 item b/c 0 indexing start
    # print the result
    print("After rolling the die 1000 times:")
    for i in range(6):
        probability = scores[i] / n
        print(f"probability of rolling a {i + 1}: {probability:.4f}") #chatgpt
    #JES MISSING CODE (done)


def main2():
    """
    This function rolls a fair die 10000 times and tallys the number of 1's, 2's etc.  Finally,
    it calculates and outputs the probability of each possible score.
    :return: nothing
    """
    #JES MISSING CODE #done
    scores = [0] * 6
    n = 10000
    for i in range(n):
        score = rfd()
        scores[score - 1] += 1

    print("After rolling a die 10000 times:")
    for i in range(6):
        probability = scores[i] / n
        print(f"probability of rolling a {i + 1}: {probability:.4f}")
    pass


def main3():
    """
    This function rolls an unfair die 10000 times and tallys the number of 1's, 2's etc.  Finally,
    it calculates and outputs the probability of each possible score.
    :return: nothing
    """
    #JES MISSING CODE
    from Die import rollUnFairDie as rud

    scores = [0] * 6
    n = 10000
    for i in range(n):
        score = rud()
        scores[score - 1] += 1

    print("After rolling die 10000 times:")
    for i in range(6):
        probability = scores[i] / n
        print(f"probability of rolling a {i + 1}: {probability:.4f}")

    pass


# endregion

# this if statement prevents these calls if this file is imported as a module.
if __name__ == "__main__":
    main()
    main2()
    main3()
