'''
All Domains > Python > Basic Data Types
https://www.hackerrank.com/domains/python/py-basic-data-types/difficulty/all/page/1
'''

from profilehooks import profile


def lists():
    '''
    Consider a list (list = []). You can perform the following commands:
    1. insert i e: Insert integer e at position i.
    2. print: Print the list.
    3. remove e: Delete the first occurrence of integer e.
    4. append e: Insert integer e at the end of the list.
    5. sort: Sort the list.
    6. pop: Pop the last element from the list.
    7. reverse: Reverse the list.

    Initialize your list and read in the value of n
    followed by n lines of commands where each command will be
    of the 7 types listed above.
    Iterate through each command in order and
    perform the corresponding operation on your list.
    '''
    nums_list = []
    for _ in range(int(input())):
        command = input().split()
        if command[0] == "print":
            print(nums_list)
        else:
            eval("nums_list." + command[0] + "(" + ",".join(command[1:]) + ")")


def tuples():
    '''
    Given an integer n, and n space-separated integers as input,
    create a tuple t, of those n integers.
    Then compute and print the result of hash(t).
    '''
    n = input()
    print(hash(tuple(list(map(int, input().split())))))


def list_comprehensions():
    '''
    You are given three integers X, Y and Z
    representing the dimensions of a cuboid.
    You have to print a list of all possible coordinates on a 3D grid
    where the sum of X_i + Y_i + Z_i is not equal to N.
    If X = 2, the possible values of X_i can be 0, 1 and 2.
    The same applies to Y and Z.
    '''
    X, Y, Z, N = (int(input()) for _ in range(4))

    print([[x, y, z]
           for x in range(X + 1) for y in range(Y + 1) for z in range(Z + 1)
           if x + y + z != N])


# @profile
def find_the_second_largest_mine():
    '''
    You are given N numbers.
    Store them in a list and find the second largest number.
    '''
    n = int(input())
    numbers = [int(x) for x in input().split()]
    max_value = max(numbers)
    numbers = [x for x in numbers if x != max_value]
    print(max(numbers))


# @profile
def find_the_second_largest_1():
    '''
    You are given N numbers.
    Store them in a list and find the second largest number.
    '''
    n, a = int(input()), list(set([int(x) for x in input().split()]))
    print(sorted(a)[len(a) - 2])


def nested_lists():
    '''
    Given the names and grades for each student in a Physics class of
    N students, store them in a nested list and
    print the name(s) of any student(s) having the second lowest grade.

    Note: If there are multiple students with the same grade,
    order their names alphabetically and print each name on a new line.
    '''
    n = int(input())
    students = []
    first = 100
    second = 100
    for _ in range(n):
        name = input()
        score = float(input())
        if score < first:
            second = first
            first = score
        elif score < second and score != first:
            second = score
        students.append([name, score])

    second_students = [s[0] for s in students if s[1] == second]
    for student in sorted(second_students):
        print(student)


def nested_lists_minimal():
    '''
    Same as before with minimal lines of code.
    '''
    students = [[input(), float(input())] for _ in range(int(input()))]
    second = sorted([s[1] for s in students])[1]
    print('\n'.join(sorted([s[0] for s in students if s[1] == second])))


def find_the_percentage():
    '''
    You have a record of N students.
    Each record contains the student's name,
    and their percent marks in Maths, Physics and Chemistry.
    The marks can be floating values.
    The user enters some integer N
    followed by the names and marks for N students.
    You are required to save the record in a dictionary data type.
    The user then enters a student's name.
    Output the average percentage marks obtained by that student,
    correct to two decimal places.
    '''
    students = {}
    for _ in range(int(input())):
        student = input().split()
        students[student[0]] = [float(s) for s in student[1:]]
    scores = students[input()]
    print('%.2f' % (sum(scores) / len(scores)))


# lists()
# tuples()
# list_comprehensions()
# find_the_second_largest_number_mine()
# find_the_second_largest_number_1()
# nested_lists()
# nested_lists_minimal()
find_the_percentage()
