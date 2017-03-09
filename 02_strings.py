'''
All Domains > Python > Strings
https://www.hackerrank.com/domains/python/py-strings/difficulty/all/page/1
'''

from profilehooks import profile


def swap_case():
    '''
    You are given a string S. Your task is to swap cases.
    In other words, convert all lowercase letters
    to uppercase letters and vice versa.
    '''
    print(input().swapcase())


def split_and_join():
    '''
    You are given a string.
    Split the string on a " " (space) delimiter and join using a - hyphen.
    '''
    print('-'.join(input().split()))


def whats_your_name():
    '''
    You are given the first name and last name of a person
    on two different lines.
    Your task is to read them and print the following:
    "Hello <firstname> <lastname>! You just delved into python."
    '''
    print("Hello %s %s! You just delved into python." % (input(), input()))


def mutations():
    '''
    Read a given string,
    change the character at a given index and then print the modified string.
    '''
    string = input()
    index, new_char = input().split()
    print(string[:int(index)] + new_char + string[int(index) + 1:])


def find_a_string():
    '''
    In this challenge, the user enters a string and a substring.
    You have to print the number of times that
    the substring occurs in the given string.
    String traversal will take place from left to right,
    not from right to left.
    '''
    string, search = (input() for _ in range(2))
    found = 0
    for i in range(len(string) - len(search) + 1):
        if string[i:i + len(search)] == search:
            found += 1
    print(found)


def find_a_string_regex():
    '''
    Solves the previous problem with using regular expression
    '''
    import re

    string, search = (input() for _ in range(2))
    match = re.findall('(?=' + search + ')', string)
    print(len(match))


# @profile
def string_validators():
    '''
    You are given a string S.
    Your task is to find out if the string S contains:
    alphanumeric characters, alphabetical characters, digits,
    lowercase and uppercase characters.
    '''
    string = input()
    alphanum, alpha, digit, lower, upper = False, False, False, False, False
    for char in string:
        if not alphanum and char.isalnum():
            alphanum = True
        if not alpha and char.isalpha():
            alpha = True
        if not digit and char.isdigit():
            digit = True
        if not lower and char.islower():
            lower = True
        if not upper and char.isupper():
            upper = True

    print(alphanum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)


# @profile
def string_validators_minimal():
    '''
    Same as before with minimal lines of code.
    '''
    string = input()
    print(any([char.isalnum() for char in string]))
    print(any([char.isalpha() for char in string]))
    print(any([char.isdigit() for char in string]))
    print(any([char.islower() for char in string]))
    print(any([char.isupper() for char in string]))


def text_alignment():
    '''
    You are given a partial code that is used for
    generating the HackerRank Logo of variable thickness.
    Your task is to replace the blank (______)
    with rjust, ljust or center.
    '''
    # Replace all ______ with rjust, ljust or center.
    # This must be an odd number
    thickness = int(input())
    c = 'H'

    # Top Cone
    for i in range(thickness):
        print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

    # Top Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) +
              (c * thickness).center(thickness * 6))

    # Middle Belt
    for i in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))

    # Bottom Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) +
              (c * thickness).center(thickness * 6))

    # Bottom Cone
    for i in range(thickness):
        print(((c * (thickness - i - 1)).rjust(thickness) + c +
               (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))


def text_wrap():
    '''
    You are given a string S and width w.
    Your task is to wrap the string into a paragraph of width w.
    '''
    import textwrap
    print(textwrap.fill(input(), int(input())))


def designer_door_mat():
    '''
    Mr. Vincent works in a door mat manufacturing company.
    One day, he designed a new door mat with the following specifications:
    - Mat size must be N x M.(N is an odd natural number, and M is 3 times N.)
    - The design should have 'WELCOME' written in the center.
    - The design pattern should only use |, . and - characters.

    More than  lines of code will result in a score of 0.
    Comment lines are counted.
    Blank lines are not counted.
    '''
    N, M = [int(x) for x in input().split()]
    for i in range(1, N, 2):
        print('-' * int((N - i) * 1.5) + '.|.' * i + '-' * int((N - i) * 1.5))
    print('-' * int(M / 2 - 3.5) + 'WELCOME' + '-' * int(M / 2 - 3.5))
    for i in range(N - 2, -1, -2):
        print('-' * int((N - i) * 1.5) + '.|.' * i + '-' * int((N - i) * 1.5))


def designer_door_mat_alt():
    '''
    Same as above.
    '''
    N, M = [int(x) for x in input().split()]
    for i in range(1, N, 2):
        print(('.|.' * i).center(M, '-'))
    print('WELCOME'.center(M, '-'))
    for i in range(N - 2, -1, -2):
        print(('.|.' * i).center(M, '-'))


def string_formatting():
    '''
    Given an integer n,
    print the following values for each integer i from 1 to n:
    1. Decimal
    2. Octal
    3. Hexadecimal (capitalized)
    4. Binary
    The four values must be printed on a single line
    in the order specified above for each i from 1 to n.
    Each value should be space-padded
    to match the width of the binary value of n.
    '''
    n = int(input())
    for i in range(1, n + 1):
        print('{0:{1}d} {0:{1}o} {0:{1}X} {0:{1}b}'.format(
            i, len(format(n, 'b'))))


def alphabet_rangoli():
    '''
    You are given an integer, N.
    Your task is to print an alphabet rangoli of size N.
    (Rangoli is a form of Indian folk art based on creation of patterns.)
    The center of the rangoli has the first alphabet letter a,
    and the boundary has the Nth alphabet letter (in alphabetical order).
    '''
    n = int(input())
    lines = []
    for i in range(n):
        line = [chr(x) for x in range(97 + n - 1, 97 + n - 2 - i, -1)]
        line += line[-2::-1]
        line = ('-'.join(line)).center(4 * n - 3, '-')
        lines.append(line)
    print('\n'.join(lines + lines[-2::-1]))


def capitalize():
    '''
    You are given a string S.
    Your task is to capitalize each word of S.
    '''
    # import re
    # print(' '.join([x.capitalize() for x in re.split(' ', input())]))
    print(' '.join([x.capitalize() for x in input().split(' ')]))


def the_minion_game():
    '''
    Kevin and Stuart want to play the 'The Minion Game'

    Both players are given the same string, S.
    Both players have to make substrings using the letters of the string S.
    Stuart has to make words starting with consonants.
    Kevin has to make words starting with vowels.
    The game ends when both players have made all possible substrings.

    A player gets 1 point for each occurrence of the substring in the string S.

    BANANA -> Stuart 12
    BANAASA -> Draw
    '''
    vowels = 'aeiou'
    kevin, stuart = 0, 0
    string = input().lower()

    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    if stuart > kevin:
        print('Stuart {}'.format(stuart))
    elif kevin > stuart:
        print('Kevin {}'.format(kevin))
    else:
        print('Draw')


def merge_the_tools():
    '''
    Consider the following:
    - A string, s, of length n where s = c_0c_1...c_n.
    - An integer, k, where k is a factor of n.
    We can split s into n/k subsegments where each subsegment, t_i,
    consists of a contiguous block of k characters in s.
    Then, use each t_i to create string u_i such that:
    - The characters in u_i are a subsequence of the characters in t_i.
    - Any repeat occurrence of a character is removed from the string
      such that each character in u_i occurs exactly once.
      In other words, if the character at some index j in t_i
      occurs at a previous index < j in t_i,
      then do not include the character in string u_i.

    Given s and k, print n/k lines where each line i denotes string u_i.
    '''
    string = input()
    k = int(input())
    for i in range(0, len(string), k):
        substring = string[i:i + k]
        to_print = ''
        for char in substring:
            if char not in to_print:
                to_print += char
        print(to_print)


# swap_case()
# split_and_join()
# whats_your_name()
# mutations()
# find_a_string()
# find_a_string_regex()
# string_validators()
# string_validators_minimal()
# text_alignment()
# text_wrap()
# designer_door_mat_alt()
# string_formatting()
# alphabet_rangoli()
# capitalize()
# the_minion_game()
merge_the_tools()
