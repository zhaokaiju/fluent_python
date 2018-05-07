"""
改进版的计时装饰器

改进的地方：
    1.支持关键字参数
    2.不遮盖被装饰函数的__name__和__doc__属性。（元属性）
"""

import time
from functools import wraps


def clock(func):
    @wraps(func)
    def clocked(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        name = func.__name__
        arg_list = []
        if args:
            arg_list.append(", ".join(repr(arg) for arg in args))

        if kwargs:
            pairs = ["%s=%r" % (k, w) for k, w in sorted(kwargs.items())]
            arg_list.append(", ".join(pairs))

        args_str = ", ".join(arg_list)
        print("[%0.8fs] %s(%s) -> %r" % (end_time - start_time, name, args_str, result))
        return result

    return clocked


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
