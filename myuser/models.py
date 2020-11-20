from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class MyUser(AbstractUser):
    display_name = models.CharField(blank=True, null=True, max_length=50)
    age = models.IntegerField(blank=True, null=True)
    homepage = models.URLField(blank=True, null=True)
