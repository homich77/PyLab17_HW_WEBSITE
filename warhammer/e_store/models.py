from django.db import models


class Category(models.Model):
    PRODUCT_CATEGORIES = (
        ('figures', 'figures'),
        ('terrains', 'terrains'),
        ('books', 'books'),
        ('painting', 'painting'),
        ('digital', 'digital'),
    )
    title = models.CharField(max_length=10, choices=PRODUCT_CATEGORIES, default='figures')
    image = models.ImageField(blank=True, upload_to='media/images/')

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    image = models.ImageField(blank=True, upload_to='media/images/')
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Cart(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(Product, through='Order')
    STATUS_CHOICES = (('open', 'open'), ('canceled', 'canceled'))
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return str('ORDER №' + self.pk + ', STATUS: ' + str(self.status) + ', DATE: ' + str(self.date))


class Order(models.Model):
    order = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Product)
    quantity = models.PositiveSmallIntegerField(default=1)

    def get_order_price(self):
        return self.item.price * self.quantity

    order_price = property(get_order_price)
