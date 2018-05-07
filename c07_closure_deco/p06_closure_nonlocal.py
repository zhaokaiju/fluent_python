"""
nonlocal声明：
    把变量标记为自由变量，即使在函数中为变量赋予新值了，也会变成自由变量。
"""


def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


def use_make_averager():
    avg = make_averager()
    print(avg(10))
    print(avg(12))
    # 输出结果：
    """
    10.0
    11.0
    """


if __name__ == '__main__':
    use_make_averager()
