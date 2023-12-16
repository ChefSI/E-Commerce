from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=107)   
    description =  models.CharField(max_length=107, default='SOME STRING')    
    USERNAME_FIELD ="email"
    REQUIRED_FIELDS =['username']

    def _str_(self):
       return self.username
    