
from django.db import models
from django.contrib.auth.models import User
from Users.models import Account
class Admin(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    # Add additional admin fields as needed

    def __str__(self):
        return self.user.username