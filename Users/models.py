

# # Create your models here.
from django.contrib.auth.models import UserManager,AbstractBaseUser,PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True


    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(("super user must have is_staff true"))
        return self.create_user(email, password, **extra_fields)

class Account(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=40,blank=True,null=True,unique=True)
    email = models.EmailField(unique=True)
    
    account_types=(('Buyer','Buyer'),('Seller','Seller'),('Admin','Admin'))
    account_type = models.CharField(max_length=30,choices=account_types,null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    
    objects = UserManager()
    
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email']

    def __str__(self):
        return str(self.username)
