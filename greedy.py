#!/usr/bin/env python

import sys


COINS = [200, 100, 50, 20, 20, 10, 5, 2, 1]


def _get_change(value):
    change = []
    current = value
    while current > 0:
        for coin in COINS:
            if coin <= current:
                change.append(coin)
                current -= coin
                break
    return change


def _main():
    if len(sys.argv) != 2:
        print "Error: Usage"
        print "./greedy.py <value>"
        sys.exit(1)

    value = int(sys.argv[1])
    print _get_change(value)


if __name__ == "__main__":
    _main()
