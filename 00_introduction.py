'''
All Domains > Python > Introduction
https://www.hackerrank.com/domains/python/py-introduction
'''


def say_hello_world_with_python():
    '''
    Print Hello, World! to stdout.
    '''
    print("Hello, World!")


def reading_raw_input():
    '''
    Read a line of input from stdin and save it to a variable s.
    Then print the contents of s to stdout.
    '''
    print(input())


def python_if_else():
    '''
    Given an integer N, perform the following conditional actions:
      If N is odd, print Weird
      If N is even and in the inclusive range of  to , print Not Weird
      If N is even and in the inclusive range of  to , print Weird
      If N is even and greater than , print Not Weird
    '''
    N = int(input().strip())
    if N % 2 == 1:
        print("Weird")
    else:
        if N == 2 or N == 4:
            print("Not Weird")
        elif N in range(6, 21):
            print("Weird")
        else:
            print("Not Weird")


def arithmetic_operators():
    '''
    Read two integers from STDIN and print three lines where:
      The first line contains the sum of the two numbers.
      The second line contains the difference of the two numbers.
      The third line contains the product of the two numbers.
    '''
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)


def python_division():
    '''
    Read two integers and print two lines.
    The first line should contain integer division.
    The second line should contain float division.

    You don't need to perform any rounding or formatting operations.
    '''
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)


def loops():
    '''
    Read an integer N.
    For all non-negative integers i < N, print i^2.
    '''
    N = int(input())
    for i in range(N):
        print(i**2)


def is_leap(year):
    '''
    You are given the year, and you have to write a function to check
    if the year is leap or not.
    '''
    leap = False
    # Write your logic here
    if year % 4 == 0:
        leap = True
    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
        else:
            leap = False
    return leap


def print_function():
    '''
    Read an integer N.
    Without using any string methods, try to print the following:
    123...N
    Note that "..." represents the values in between.
    '''
    print(*[x for x in range(1, int(input()) + 1)], sep="")

# say_hello_world_with_python()
# reading_raw_input()
# python_if_else()
# arithmetic_operators()
# python_division()
# loops()
# is_leap(1980)
# print_function()
