from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name



