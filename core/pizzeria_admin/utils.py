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


def generate_dummy_daily_orders(limit_per_day=50):
    items = Item.objects.all()
    for i in range(1, 31):
        random_limit_per_day = random.randint(1, limit_per_day)
        for j in range(random_limit_per_day):
            order = Order.objects.create(
                ordered_on=datetime.date(2021, 1, i),
                order_status="Paid"
            )
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
                f'Day: {i} Order: {j} LimitPerDay: {random_limit_per_day} Created', end="\r")


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


def get_min_max_year():
    # Returns a tuple containing the min and max year
    # to be used while rendering the statistics page
    CURRENT_YEAR = get_present_year()
    remainder = CURRENT_YEAR % 10
    min_year = CURRENT_YEAR - remainder
    max_year = min_year + 10
    return min_year, max_year


def make_new_year_range():
    # Returns a generator range object for the range of years
    # to be used while rendering the statistics page
    min_year, max_year = get_min_max_year()
    return range(min_year, max_year+1)


def get_daily_data():
    # Returns a tuple containing the labels and data
    # for the daily chart
    month = get_present_month()
    orders_by_month = Order.objects.filter(ordered_on__month=month)
    label = [i for i in generate_labels_for_month(month)]
    data = [len(orders_by_month.filter(ordered_on__day=i))
            for i in range(1, 31)]
    return label, data


def get_weekly_data():
    # Returns a tuple containing the labels and data
    # for the weekly chart
    month = get_present_month()
    orders_by_month = Order.objects.filter(ordered_on__month=month)
    label = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']
    data = [len(orders_by_month.filter(ordered_on__day=i))
            for i in range(1, 8)]
    return label, data


def get_monthly_data():
    # Returns a tuple containing the labels and data
    # for the monthly chart
    orders = Order.objects.all()
    label = ['Jan', 'Feb', 'Mar', 'Apr', 'May',
             'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    data = [len(orders.filter(ordered_on__month=i)) for i in range(1, 13)]
    return label, data


def get_yearly_data():
    # Returns a tuple containing the labels and data
    # for the yearly chart
    orders = Order.objects.all()
    label = list(make_new_year_range())
    data = [len(orders.filter(ordered_on__year=i)) for i in label]
    return label, data
