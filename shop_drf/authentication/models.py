import email
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models.fields import BooleanField

from .managers import UserManager
from core.models import TimestampedModel

# Create your models here.
class User(AbstractBaseUser,PermissionsMixin,TimestampedModel):
    username = models.CharField(max_length=255,unique=True)
    email = models.EmailField(db_index=True,unique=True)
    phone_number = models.CharField(max_length=255)
    is_active= BooleanField(default=True)
    is_staff= BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = [
        'username',
        'phone_number'
    ]
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.username
    
    def get_short_name(self):
        return self.username
        
    
    