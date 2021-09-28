# recursiveFibFunction.py
"""
title: Recursive Fibonacci Sequence Generator
author: Ayden Hogeveen
date-created: 2021-09-27

This is a project I started working on after I finished all my assignments for my computer science lab,
I am currently also working on a chess engine, and I had heard of big O notation before, in relation to
efficient algorithms, and I wanted to create a simple algorithm and optimize it, and then use that to make
an efficient move-generation method in my other project.
"""
import time

known_fib = {
    0: 1,
    1: 1
    }


def getFibNum(num):
    """
    Returns the Fibonacci number based on the index number provided
    - Using a dictionary, the function can now store the numbers generated, and
    access them again later, without wasting time parsing identical trees
    """
    if num in known_fib:  # Base Cases
        return known_fib[num]

    # Find and add the Fibonacci Number
    known_fib[num] = getFibNum(num-1) + getFibNum(num-2)
    return known_fib[num]


if __name__ == '__main__':
    fib_nums = int(input("Please list amount of fib numbers that you want to see:\n> "))
    start = time.perf_counter()

    for i in range(fib_nums):
        print(f"{i+1}. {getFibNum(i+1)}")
    stop = time.perf_counter()

    print(f"{fib_nums} numbers of the sequence in {stop - start} seconds.")
