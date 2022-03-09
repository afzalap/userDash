from django.db import models
from django.contrib.auth.models import  AbstractUser
from .manager import UserManager

# Create your models here.

class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    UserType = models.CharField(max_length=30)
    phoneNo = models.CharField(max_length=10, unique=True, default='Anonymous')
    dob = models.DateField(null=True)
    USERNAME_FIELD = 'phoneNo'
    REQUIRED_FIELDS = []

    objects = UserManager()



    




