#Prove by Calculations the gambler ruin problem in the bitcoin 

#The probability of an attacker catching up from a given deficit

# p - probability an honest node finds the next block
# q - probability the attacker finds the next block
# qz - probability the attacker will ever catch up from z blocks behind

import math

q = float(input("Probability of the attacker finds the next block "))
z = int(input("How many blocks is the attacker behind "))


def attackerSuccessProbability(q,z):
    x = range(0,z+1)
    p = 1 - q
    lambda_n = z * (q/p)
    sum_n = 1

    for n in x:
        poisson = math.exp(-lambda_n)
        x_inside = range(1,n+1)
        for n_inside in x_inside:
            poisson = poisson * (lambda_n/n_inside)
        sum_n = sum_n - poisson * (1 - math.pow(q/p,z-n)) 
        print("Block nº " + str(n) + " ----> " + str(sum_n))
    return sum_n


attackerSuccessProbability(q,z)
