from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

class Cart(models.Model):
    products = models.ManyToManyField(Product, related_name='cart_items', blank=True)
    
    def total_price(self):
        return sum([product.price for product in self.products.all()])