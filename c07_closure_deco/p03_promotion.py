"""
使用装饰器改进“策略”模式

案例：
    电商促销，最大优惠
"""

promos = []


def promos(func):
    promos.append(func)
    return func


@promos
def fidelity(order):
    """
    为积分1000或以上的顾客提供5%折扣
    """
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


@promos
def bulk_time(order):
    """
    单个商品为20个或以上时提供10%折扣
    """
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount


@promos
def large_order(order):
    """
    订单中的不同商品达到10个或以上时提供7%折扣
    """
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0


def best_promo(order):
    """
    选择可用的最佳折扣
    """
    return max(promo(order) for promo in promos)
