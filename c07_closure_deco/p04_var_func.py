"""
Python的设计选择：
    Python不要求声明变量，但是假定在函数定义体中赋值的变量是局部变量。
"""
y = 1


def func(x):
    global y
    print(x)
    print(y)
    y = 10


def use_func():
    func(2)
    print(y)
    # 输出结果：
    """
    2
    1
    10
    """


if __name__ == '__main__':
    use_func()
