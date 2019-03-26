#!/usr/bin/python

import sys


def making_change(amount, denominations):
    # base cases
    if amount < 0:
        return 0
    elif amount <= 1:
        return 1
    # creates a set for memoization
    ways = [1]+[0]*amount
    # loops through each coin in the list of denominations
    for coin in denominations:
        # for each number in the range
        for i in range(coin, amount+1):
            # increments the ways set for each coin and adds them
            ways[i] += ways[i-coin]
    return ways[amount]

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print('''There are {ways} ways to make {amount} cents.
        '''.format(ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
