from django.db import models
from users.models import User

# Create your models here.
class RootCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    root_category = models.ForeignKey(RootCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Color(models.Model):
    name = models.CharField(max_length=110)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=110)

    def __str__(self):
        return self.name        


class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    prices = models.IntegerField() 
    info = models.TextField()
    colors = models.ManyToManyField(Color)
    sizes = models.ManyToManyField(Size)
    discount = models.PositiveIntegerField(null=True, blank=True)
    is_week_product = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    quantity = models.PositiveIntegerField()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=[
        (1, 'Joylandi'),
        (2, 'Tayyorlandi'),
        (3, 'Yuborildi'),
        (4, 'Yetkazildi')
    ], default=1)  


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()