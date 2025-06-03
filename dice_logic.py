import random
from math import comb

def roll_dice(num_dice):
    """Roll num_dice d6 dice and return the results"""
    return [random.randint(1, 6) for _ in range(num_dice)]

def count_successes(dice_results):
    """Count the number of 6s (successes) in the dice results"""
    return sum(1 for die in dice_results if die == 6)

def calculate_probability(num_dice, successes):
    """Calculate the probability of getting exactly 'successes' successes with 'num_dice' dice"""
    # Probability of success on a single die (rolling a 6)
    p_success = 1/6
    # Probability of failure on a single die (rolling 1-5)
    p_failure = 5/6
    
    # Binomial probability formula
    probability = comb(num_dice, successes) * (p_success ** successes) * (p_failure ** (num_dice - successes))
    return probability * 100