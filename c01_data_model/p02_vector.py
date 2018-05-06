from math import hypot


class Vector:
    """
    二维向量
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        """
        字符串表现形式（调试和记录日志）
        """
        return "Vector(%r, %r)" % (self.x, self.y)

    # def __str__(self):
    #     """
    #     字符串 （给终端用户查看）
    #     """
    #     return "({x}, {y})".format(x=self.x, y=self.y)

    def __abs__(self):
        """
        绝对值
        """
        return hypot(self.x, self.y)

    def __bool__(self):
        """
        布尔值
        """
        return bool(self.x or self.y)

    def __add__(self, other):
        """
        加法
        """
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other):
        """
        乘法
        """
        return Vector(self.x * other.x, self.y * other.y)


def use_vector():
    vector1 = Vector(1, 1)
    vector2 = Vector(2, 3)
    # 加法
    print(vector1 + vector2)
    # 绝对值
    print(abs(vector1))
    # 布尔值
    print(bool(vector1))
    # 乘法
    print(vector1 * vector2)
    # 输出结果：
    """
    Vector(3, 4)
    1.4142135623730951
    True
    Vector(2, 3)
    """


if __name__ == '__main__':
    use_vector()
