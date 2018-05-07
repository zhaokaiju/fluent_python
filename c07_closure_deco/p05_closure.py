"""
闭包：
    闭包指延伸了作用域的函数，其中包含函数定义体中引用、但是不在定义体中定义的非全局变量。
    函数是不是匿名的没关系，关键是它能访问定义体之外定义的非全局变量。
"""


def make_averager():
    """
    闭包
    """

    # 局部变量（非全局变量）（自由变量）
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

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
