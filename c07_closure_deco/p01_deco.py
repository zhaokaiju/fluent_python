"""
装饰器通常把函数替换成另一个函数
"""


def deco(func):
    def inner():
        print("running inner")

    return inner


@deco
def target():
    print("running target()")


def use_desc():
    target()
    # 输出结果：
    """
    running inner
    """


if __name__ == '__main__':
    use_desc()
