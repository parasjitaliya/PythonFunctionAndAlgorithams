# -------------------Power of two--------------------
def power_of_2(power):
    # ittretion for increment the number for pwore
    for i in range(power + 1):
        print(f"2^{i}={2 ** i}")


# ------------------Leap Year -----------------------


def checkyear(year):
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))


# --------------------Harmonic Number ------------------
def harmonic(number):
    # initialize vale of variable
    harmonic = 1
    # ittration of number start with 2
    for i in range(2, number + 1):
        harmonic = harmonic + 1 / i
        print(harmonic)


# -----------------------Prime factor ------------------------


def primefactor(number):
    # arry for store factors
    primefactors = []
    # condition for number check
    while number > 1:
        for i in range(2, number + 1):
            if number % i == 0:
                number = number // i
                primefactors.append(i)
                break;
    return primefactors


# ------------------------gambler logic ----------------------


def gambler(stake, goal):
    import random
    bets = 0
    win = 0
    # for i in range(time_ta_play)
    while win != goal and stake != 0:
        num = random.random()
        if num < 0.5:
            bets = bets + 1
            win = win + 1
        else:
            bets = bets + 1
            stake = stake - 1
    loss_percentage = ((bets - win) / bets) * 100
    win_percentage = (win / bets) * 100
    print(f"Total number of bets = {bets}")
    print(f"Total win = {win}")
    print(f"win percentage  ={win_percentage}")
    print(f"loss percentage ={loss_percentage}")


# ------------------------Coupon generations-----------------

import random


def number_coupons(number):
    distinct_coupons = []
    count = 0

    while len(distinct_coupons) < number:
        # Generate a random number
        randomNumber = random.randint(1, number)

        # If generated coupon is already exist into list then we not add that coupon into list
        if randomNumber not in distinct_coupons:
            distinct_coupons.append(randomNumber)

        count += 1

    return count

#---------------------------Three number sum is zero-------------------

def numbersum(listnum):
    print(listnum)
    for first in range(0, len(listnum)):
        for second in range(first + 1, len(listnum)):
            for third in range(second + 1, len(listnum)):
                sum = listnum[first] + listnum[second] + listnum[third]
                if sum == 0:
                    print(f'{listnum[first]}+{listnum[second]}+{listnum[third]} = {sum}')

#-------------------------- distance from the point (x, y) to the origin (0, 0) --------------------


import math


def distance_from_point(x,y):
    distance = math.sqrt(math.pow(x,2) + math.pow(y,2));
    return distance