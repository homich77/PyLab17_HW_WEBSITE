from django.db import models
from e_store.models import Product


class Cart(models.Model):
    items = models.ForeignKey(Product)
    amount = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        self.price = self.items.price * self.amount
        super(Cart, self).save(*args, **kwargs)


def get_total_price():
    return sum(item.price for item in Cart.objects.all())
