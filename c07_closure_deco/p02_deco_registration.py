"""
装饰器的一个关键特性是，它们在被装饰的函数定义之后立即执行。
"""

register_list = []


def register(func):
    print("running register(%s)" % func)
    register_list.append(func)
    return func


@register
def f1():
    print("running f1()")


@register
def f2():
    print("running f2()")


def f3():
    print("running f3()")


def use_register():
    print(register_list)
    f1()
    f2()
    f3()
    # 输出结果：
    """
    running register(<function f1 at 0x10c50d730>)
    running register(<function f2 at 0x10c50d7b8>)
    [<function f1 at 0x10c50d730>, <function f2 at 0x10c50d7b8>]
    running f1()
    running f2()
    running f3()
    """


if __name__ == '__main__':
    use_register()
