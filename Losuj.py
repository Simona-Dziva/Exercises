import random

#generate 5 random numbers between 10-30
def losuj_sportku(pocet_cisel=6, od=1, do=49):
    # do +1 -> because the range excludes the right value
    return random.sample(range(od, do + 1), pocet_cisel)

    for i in range(5):
        print(losuj_sportku)