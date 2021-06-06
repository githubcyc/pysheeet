from itertools import count, islice, cycle, repeat

"""
https://docs.python.org/3/library/itertools.html
1. Infinite iterators
"""


def infinite_iterators():
    for i in islice(count(0, 2), 3):
        print(i)
        if i > 5:
            break

    for i, s in enumerate(cycle('ABC')):
        print(s)
        if i > 3:
            break

    for i in repeat(10, 3):
        print(i)


if __name__ == '__main__':
    infinite_iterators()
