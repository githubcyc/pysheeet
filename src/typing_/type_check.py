# give a type hint
from typing import Generator


def fib(n: int) -> Generator:
    a: int = 0
    b: int = 1
    for _ in range(n):
        yield a
        b, a = a + b, b


if __name__ == '__main__':
    print([n for n in fib(3.0)])
