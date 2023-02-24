from .models import Order
from datetime import datetime


def new_order_id(request):
    #  Returns new_order_id and new_order_date
    orders = Order.objects.all()
    new_order_id = 1
    if orders:
        last_order = orders[len(orders) - 1]
        new_order_id = last_order.id + 1
    new_order_date = datetime.now()
    return {
        'new_order_id': new_order_id,
        'new_order_date': new_order_date,
    }
