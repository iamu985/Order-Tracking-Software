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


def all_orders(request):
    #  Returns all orders
    orders = Order.objects.filter(is_new=False).order_by('-ordered_on')
    total_orders = len(orders)
    print("IN all orders")
    if orders:
        context = {
            'orders': orders,
            'length': total_orders,
        }
    context = {
        'orders': orders,
        'length': total_orders,
    }
    return context
