"""
使用functools.lru_cache做备忘
"""

from functools import lru_cache

from p08_deco_improve_clock import clock


@clock
def fibonacci(n):
    if n < 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def use_fibonacci():
    fibonacci(3)
    # 输出结果：
    """
    [0.00025240s] fibonacci(1) -> 1
    [0.00000496s] fibonacci(0) -> 1
    [0.00039627s] fibonacci(2) -> 2
    [0.00000451s] fibonacci(1) -> 1
    [0.00047190s] fibonacci(3) -> 3
    """


@lru_cache()
@clock
def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def use_fib():
    fib(3)
    # 输出结果：
    """
    [0.00000274s] fib(1) -> 1
    [0.00000288s] fib(0) -> 1
    [0.00004657s] fib(2) -> 2
    [0.00007188s] fib(3) -> 3
    """


@clock
def fib_gen(n):
    i, a, b = 0, 1, 1

    while i < n:
        yield b
        a, b = b, a + b
        i += 1


def use_fib_gen():
    fib = fib_gen(3)
    for item in fib:
        print(item)
    # 输出结果:
    """
    [0.00000112s] fib_gen(3) -> <generator object fib_gen at 0x10c62d0f8>
    1
    2
    3
    """


if __name__ == '__main__':
    use_fibonacci()
    use_fib()
    use_fib_gen()
