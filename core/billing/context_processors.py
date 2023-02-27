from .models import Order
from datetime import datetime


def new_order_id(request):
    #  Returns new_order_id and new_order_date
    orders = Order.objects.all()
    print(f"{orders=}")
    new_order_id = 1
    if orders:
        print("There are orders in the database")
        last_order = orders[len(orders) - 1]
        print(f"Got last order: {str(last_order)}")
        if last_order.is_new:
            print(f"new_order_id: {last_order.id}")
            return {
                "new_order_id": last_order.id,
                "new_order_date": last_order.ordered_on,
            }
        else:
            new_order_id = last_order.id + 1
            print(f"New order id: {new_order_id}")
    new_order_date = datetime.now()
    return {
        'new_order_id': new_order_id,
        'new_order_date': new_order_date,
    }


"""
Issue: Orders will return all the orders in the database.
If there are initially 3 orders, it will return all those 3 orders.
> print("There are orders in the database")
It gets the last order ie Order 3
Then returns the new_order_id to be 3 + 1 = 4

But in the add_item view, the new order id is received 4
When we add item to the Order.item_set , the order gets created and
Now the new_order_id will get increased as per the function. So the new_order_id
would be 5 without completely adding the items.
"""
