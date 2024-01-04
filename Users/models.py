from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class toolboxUser(AbstractUser):
    institution = models.CharField(max_length = 100, blank = True, null = True)