from django.db import models
from django.contrib.auth.models import User
from Users.models import Account
from seller.models import Product

class Buyer(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    # Add additional buyer fields as needed

    def __str__(self):
        return self.user.username

class Order(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.buyer.user.username}"
