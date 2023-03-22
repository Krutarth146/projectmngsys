from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin',default=False)
    is_pmanager = models.BooleanField('Is pmanager',default=False)
    is_teamleader = models.BooleanField('Is teamleader',default=False)
    is_developer = models.BooleanField('Is developer',default=False)
    is_tester = models.BooleanField('is tester',default=False)