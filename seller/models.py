from django.db import models
from django.contrib.auth.models import User
from Users.models import Account

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    seller = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
# seller/models.py


class Seller(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    # Add additional seller fields as needed

    def __str__(self):
        return self.user.username
