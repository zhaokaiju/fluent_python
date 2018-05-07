"""
计时装饰器

装饰器的典型行为：
    把被装饰的函数替换成新函数，二者接收相同的参数，而且（通常）返回被装饰的函数该返回的值，同时还会做些额外操作。
"""

import time


def clock(func):
    """
    计时装饰器
    """

    def cloked(*args):
        start_time = time.perf_counter()
        result = func(*args)
        end_time = time.perf_counter()

        name = func.__name__
        args_str = ", ".join(repr(arg) for arg in args)
        print("[%0.8fs] %s(%s) -> %r" % (end_time - start_time, name, args_str, result))
        return result

    return cloked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    """
    n阶乘
    """
    return 1 if n < 2 else n * factorial(n - 1)


def use_clock():
    snooze(1)
    factorial(3)
    # 输出结果：
    """
    [1.00247445s] snooze(1) -> None
    [0.00000528s] factorial(1) -> 1
    [0.00004957s] factorial(2) -> 2
    [0.00010084s] factorial(3) -> 6
    """


if __name__ == '__main__':
    use_clock()
