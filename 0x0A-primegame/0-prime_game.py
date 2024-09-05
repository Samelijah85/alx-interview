#!/usr/bin/python3
"""
Prime Game Module

This module defines a function to determine the winner of a prime number game
played between Maria and Ben.

Examples:
    >>> isWinner(3, [4, 5, 2])
    'Maria'
    >>> isWinner(5, [2, 5, 1, 4, 3])
    'Ben'
"""


def sieve_of_eratosthenes(max_n):
    """
    Generate a list of prime numbers up to max_n using the
    Sieve of Eratosthenes algorithm.
    """
    is_prime = [True] * (max_n + 1)
    p = 2
    while (p * p <= max_n):
        if is_prime[p]:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, max_n + 1) if is_prime[p]]
    return prime_numbers


def isWinner(x, nums):
    """Determine the winner after x rounds of the game"""
    if x <= 0 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
        else:
            if len(sieve_of_eratosthenes(n)) % 2 == 1:
                maria_wins += 1
            else:
                ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
