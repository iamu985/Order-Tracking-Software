import pytest
from .models import Order, Item


@pytest.mark.django_db
class TestModels:
    def test_order_status_is_waiting(self):
        # Create object in mock database
        obj1 = Order.objects.create()
        assert obj1.order_status == 'Waiting'

    def test_order_status_is_delivered(self):
        obj1 = Order.objects.create(order_status='Delivered')
        assert obj1.order_status == 'Delivered'

    def test_order_status_is_paid(self):
        obj1 = Order.objects.create(order_status='Paid')
        assert obj1.order_status == 'Paid'

    def test_order_paid_online_is_true(self):
        obj1 = Order.objects.create(paid_online=True)
        assert obj1.paid_online == True
