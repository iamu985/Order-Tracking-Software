import pytest
import random
from billing.models import Order, Item, OrderItem


@pytest.fixture
def order_data():
    id_ = 0
    order = Order.objects.create(pk=id_)
    return order


@pytest.fixture
def item_data():
    item = Item.objects.create(pk=0,
                               name="Mock Tea",
                               price="100")
    return item


@pytest.fixture
def multilple_items():
    items = []
    seed = random.randint(1, 7)
    for i in range(seed):
        item = Item.objects.create(id=i,
                                   name=f'Item{i}',
                                   price=10)
        items.append(item)
    return items


@pytest.fixture
def order_item_data(order_data, multilple_items):
    print(order_data)

    for items in multilple_items:
        order_data.items.add(items)
    return order_data


@pytest.fixture
def orderitem_data(order_data, item_data):
    orderitem = OrderItem.objects.create(order=order_data,
                                         item=item_data,
                                         quantity=3)
    return orderitem


@pytest.fixture
def item_name():
    name = "Chicken Fried Rice"
    id_ = 0
    price = 10
    return Item.objects.create(id=id_,
                               name=name,
                               price=price)
