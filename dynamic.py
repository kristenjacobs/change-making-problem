#!/usr/bin/env python

import sys


def _get_change(denominations, value, cache):
    if value == 0:
        return []

    if value in cache:
        return cache[value]

    min_length_so_far = sys.maxint
    for coin in denominations:
        if coin <= value:
            new_change = [coin] + _get_change(denominations, value - coin, cache)
            if len(new_change) < min_length_so_far:
                shortest_so_far = new_change
                min_length_so_far = len(shortest_so_far)
    cache[value] = shortest_so_far
    return shortest_so_far


def _main():
    if len(sys.argv) < 2:
        print "Error: Usage"
        print "./general.py <value> <coin1> <coin2> <coin3> ... "
        sys.exit(1)

    value = int(sys.argv[1])
    denominations = map(int, sys.argv[2:])
    print _get_change(denominations, value, {})


if __name__ == "__main__":
    _main()
