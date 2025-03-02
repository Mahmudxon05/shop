from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=13, unique=True, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    type = models.IntegerField(choices=[
         (1,'adminstrator'),
         (2, 'manager'),
         (3, 'customer')
    ], default=3)

    def __str__ (self):
            return self.username
    
    class Meta(AbstractUser.Meta):
          swappable = 'AUTH_USER_MODEL'
          verbose_name = 'User'
          verbose_name_plural = 'Foydalanuvchilar'

          def __str__(self):
            return self.verbose_name 

  
