import datetime
import random
from billing.models import Item, Order, OrderItem


def get_present_month():
    return datetime.datetime.today().month


def get_present_day():
    return datetime.datetime.today().weekday()


def get_present_date():
    return datetime.datetime.today().date()


def get_present_year():
    return datetime.datetime.today().year


def generate_labels_for_month(month: int):
    thirty_months = [4, 6, 9, 11]
    thirty_one_months = [1, 3, 5, 7, 8, 19, 12]
    year = get_present_year()
    month = get_present_month()
    if not year % 4 and month == 2:
        return range(1, 30)
    else:
        return range(1, 29)
    if month in thirty_months:
        return range(1, 31)
    if month in thirty_one_months:
        return range(1, 32)


def get_random_date():
    year = random.randint(2020, 2023)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return datetime.date(year, month, day)


def generate_dummy_orders(limit=100):
    items = Item.objects.all()
    item_limit = random.randint(1, 8)
    for i in range(limit):
        order = Order.objects.create(
            pk=i,
            ordered_on=get_random_date(),
            order_status="Paid"
        )
        for j in range(item_limit):
            item = random.choice(items)
            order_item = OrderItem.objects.create(
                order=order,
                item=item,
                quantity=random.randint(1, 5)
            )
            order_item.save()
            order.is_new = False
            order.save()
            print(
                f'Order {i} Item {j} Created|Order.isNew={order.is_new}', end="\r")
