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

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    image = models.ImageField(blank=True, upload_to='images/')
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

