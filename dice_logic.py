import random
from math import comb

def roll_dice(num_dice):
    """Roll num_dice 6-sided dice and return the results as a list."""
    return [random.randint(1, 6) for _ in range(num_dice)]

def count_successes(dice_results):
    """Count how many dice rolled a 6 (i.e., count successes)."""
    return dice_results.count(6)

def calculate_probability(num_dice, successes):
    """
    Calculate the binomial probability of rolling exactly 'successes'
    sixes with 'num_dice' 6-sided dice.
    """
    if successes > num_dice or successes < 0:
        return 0.0

    p = 1 / 6
    q = 5 / 6
    probability = comb(num_dice, successes) * (p ** successes) * (q ** (num_dice - successes))
    return probability * 100
