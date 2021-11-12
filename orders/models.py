from django.db import models
from ..usuarios.models import Customer

class Order_detail(models.Model):
    order_detail_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.order_detail_id)

class Order_item(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order_detail_id = models.ForeignKey(Order_detail, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.order_item_id)
        