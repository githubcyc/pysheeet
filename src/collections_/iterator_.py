from collections import Iterable, Iterator, Generator
from inspect import isgenerator, isgeneratorfunction, iscoroutine


if __name__ == '__main__':
    s = 'test'  # list tuple dict
    print(isinstance(s, Iterable))
    print(hasattr(s, '__iter__'))
    print(isinstance(s, Iterator))
    print(hasattr(s, '__next__'))

    print(isinstance(iter(s), Iterator))

    def gen():
        for i in range(10):
            n = yield i
            print(n)
            if n is not None:
                return
    g = gen()
    print(isgenerator(g), isgeneratorfunction(gen), iscoroutine(g))
    # send()的作用是在next()的基础上，多了个给xx赋值的功能。 next <==> send(None)
    next(g)
    g.__next__()
    print(g.send(None))
    g.send(1)
    print(isinstance(g, Generator))
    print(isinstance(g, Iterator))
