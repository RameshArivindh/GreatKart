from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class Accounts(AbstractBaseUser):
    first_name      = models.CharField(max_length = 50)
    last_name       = models.CharField(max_length = 50)
    username        = models.CharField(max_length = 50, unique=True)
    email           = models.EmailField(max_length = 100, unique=True)