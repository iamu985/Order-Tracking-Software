from django.db import models
from uuid import uuid4 as uuid

# Create your models here.


class Order(models.Model):
    ORDER_STATUS_CHOICE = [
        ('Waiting', 'Waiting'),
        ('Delivered', 'Delivered'),
        ('Paid', 'Paid'),
    ]
    ordered_on = models.DateTimeField(auto_now_add=True)
    paid_online = models.BooleanField(default=False)
    order_status = models.CharField(choices=ORDER_STATUS_CHOICE,
                                    max_length=10,
                                    default=ORDER_STATUS_CHOICE[0][0])

    def get_id(self):
        """
        Returns the id of the order
        """
        return self.pk

    def get_total_orders(self):
        """
        Returns the number total objects in the Order queryset
        """
        return len(self.objects.all())

    def get_total_price(self, order_id):
        """
        Returns the total price of the order.
        This includes the sum of the toal prices of the items that 
        are ordered.
        """
        order_obj = self.objects.get(pk=order_id)
        return sum([item.price for item in order_obj.items.all()])

    def __str__(self):
        return f"OrderId: {self.pk}"


class Item(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField(default=0)
    order = models.ManyToManyField("Order")

    def __str__(self):
        return f"{self.id}. {self.name} - Rs. {self.price}"
