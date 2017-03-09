'''
All Domains > Python > Sets
https://www.hackerrank.com/domains/python/py-sets/
'''


def introduction_to_sets():
    '''
    Ms. Gabriel Williams is a botany professor at District College.
    One day, she asked her student Mickey to compute the
    average of all the plants with distinct heights in her greenhouse.

    Formula used:
    Average = Sum of distinct heights / Total number of distinct heights.
    '''
    n, heights = input(), [int(x) for x in input().split()]
    distinct_heights = set(heights)
    print(sum(distinct_heights) / len(distinct_heights))


def symmetric_difference():
    '''
    Given 2 sets of integers, M and N,
    print their symmetric difference in ascending order.
    The term symmetric difference indicates those values
    that exist in either M or N but do not exist in both.
    '''
    input()
    M = set(input().split())
    input()
    N = set(input().split())
    # sim_dif = M.union(N).difference(M.intersection(N))
    print('\n'.join(sorted(list(M ^ N), key=int)))


def no_idea():
    '''
    There is an array of n integers.
    There are also 2 disjoint sets, A and B, each containing m integers.
    You like all the integers in set A and dislike all the integers in set B.
    Your initial happiness is 0.
    For each i integer in the array, if i is in A, you add 1 to your happiness.
    If i is in B, you add -1 to your happiness.
    Otherwise, your happiness does not change.
    Output your final happiness at the end.

    Note: Since A and B are sets, they have no repeated elements.
    However, the array might contain duplicate elements.
    '''
    n, m = input().split()
    array = input().split()
    set_a = set(input().split())
    set_b = set(input().split())
    # happiness = 0
    # for number in array:
    #     if number in set_a:
    #         happiness += 1
    #     if number in set_b:
    #         happiness -= 1
    # print(happiness)
    print(sum([1 if x in set_a else -1 if x in set_b else 0 for x in array]))


def set_add():
    '''
    Rupal has a huge collection of country stamps.
    She decided to count the total number of distinct country stamps
    in her collection. She asked for your help.
    You pick the stamps one by one from a stack of N country stamps.

    Find the total number of distinct country stamps.
    '''
    stamps = set()
    for _ in range(int(input())):
        stamps.add(input())
    print(len(stamps))


def set_discard_remove_pop():
    '''
    You have a non-empty set s,
    and you have to execute N commands given in N lines.

    The commands will be pop, remove and discard.
    '''
    n = input()
    s = set([int(x) for x in input().split()])
    for _ in range(int(input())):
        command = input().split()
        if command[0] == 'pop':
            s.pop()
        elif command[0] == 'remove':
            s.remove(int(command[1]))
        elif command[0] == 'discard':
            s.discard(int(command[1]))
    print(sum(s))


def set_union():
    '''
    The students of District College have subscriptions to
    English and French newspapers.
    Some students have subscribed only to English,
    some have subscribed to only French and
    some have subscribed to both newspapers.

    You are given two sets of student roll numbers.
    One set has subscribed to the English newspaper,
    and the other set is subscribed to the French newspaper.
    The same student could be in both sets.
    Your task is to find the total number of students
    who have subscribed to at least one newspaper.
    '''
    input()
    english = set(input().split())
    input()
    french = set(input().split())
    print(len(english.union(french)))


def set_intersection():
    '''
    The students of District College have subscriptions to
    English and French newspapers.
    Some students have subscribed only to English,
    some have subscribed only to French and
    some have subscribed to both newspapers.

    You are given two sets of student roll numbers.
    One set has subscribed to the English newspaper,
    one set has subscribed to the French newspaper.

    Your task is to find the total number of students
    who have subscribed to both newspapers.
    '''
    input()
    english = set(input().split())
    input()
    french = set(input().split())
    print(len(english.intersection(french)))


def set_difference():
    '''
    Students of District College have a subscription to
    English and French newspapers.
    Some students have subscribed to only the English newspaper,
    some have subscribed to only the French newspaper and
    some have subscribed to both newspapers.

    You are given two sets of student roll numbers.
    One set has subscribed to the English newspaper,
    and one set has subscribed to the French newspaper.

    Your task is to find the total number of students
    who have subscribed to only English newspapers.
    '''
    input()
    english = set(input().split())
    input()
    french = set(input().split())
    print(len(english.difference(french)))


def set_symmetruc_difference():
    '''
    Students of District College have subscriptions to
    English and French newspapers.
    Some students have subscribed to English only,
    some have subscribed to French only, and
    some have subscribed to both newspapers.

    You are given two sets of student roll numbers.
    One set has subscribed to the English newspaper,
    and one set has subscribed to the French newspaper.

    Your task is to find the total number of students
    who have subscribed to either the English or
    the French newspaper but not both.
    '''
    input()
    english = set(input().split())
    input()
    french = set(input().split())
    print(len(english ^ french))


def set_mutations():
    '''
    You are given a set A and N number of other sets.
    These N number of sets have to perform some
    specific mutation operations on set A.

    Your task is to execute those operations and
    print the sum of elements from set A.
    '''
    input()
    set_a = set(input().split())
    for _ in range(int(input())):
        command = (input().split())[0]
        set_temp = set(input().split())
        eval("set_a.%s(%s)" % (command, set_temp))
    print(sum([int(x) for x in set_a]))

# introduction_to_sets()
# symmetric_difference()
# no_idea()
# set_add()
# set_discard_remove_pop()
# set_union()
# set_intersection()
# set_difference()
# set_symmetruc_difference()
set_mutations()
