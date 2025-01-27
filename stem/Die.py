# region imports
#This way of importing is saying from (the module) random, import (the function) random
#Other ways of importing might be:  import random
#             In the above case, we access the function random as random.random()
#Another way to import might be:  from random import random as rnd
#             In the above case, we use rnd() to produce a random number
from random import random
from tokenize import endpats

# endregion

# region functions
def rollFairDie():
    """
    This function simulates rolling a fair die such that the probability of each integer is 1/6.
    :return: an integer between 1 and 6 inclusive
    """
    x = random() #JES MISSING CODE  # should be a floating point number between 0.0 and 1.0 (done)
    if x <= 1.0/6 : #JES MISSING CODE (done)
        return 1
    if x <= 2.0/6 :  #The word doc has these typed out as "else if". Doing that caused an error in the code.
        return 2
    if x <= 3.0/6 :
        return 3
    if x <= 4.0/6 :
        return 4
    if x <= 5.0/6 :
        return 5
    if x <= 6.0/6 :
        return 6
    #JES MISSING CODE (done)

def rollUnFairDie():
    """
    This function simulates rolling an unfair die such that the probability of rolling a 1 is 0.2. with all other
    integers having equal probability.  Now, the probability of numbers 2-6 should be 0.8/5.
    :return: an integer between 1 and 6 inclusive
    """
    p=0.3
    x= random() #JES MISSING CODE (done)
    if x <= 0.2 :#JES MISSING CODE
        return 1
    else :
        return 2 + int((x-0.2) / (0.8/5))  #got this eq. from chat gpt
    #JES MISSING CODE (done)
# endregion

# The if statement below is known as: main guarding
if __name__ == "__main__":
    x = rollFairDie()
    print(x)