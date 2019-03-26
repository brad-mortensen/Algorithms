#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    options = ['rock', 'paper', 'scissors']
    output = []
    if n <= 0:
        return [output]
    elif n == 1:
        for option in options:
            output.append([option])
        return output
    else:
        for option in options:
            output.append([])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
