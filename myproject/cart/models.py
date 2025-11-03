from django.db import models

class Cart(models.Model):
    customer = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.customer} - {self.product}"
