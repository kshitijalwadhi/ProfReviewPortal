from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Block(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    BOOL_CHOICES = ((False, 'No'), (True, 'Yes'))
    block = models.BooleanField(choices=BOOL_CHOICES, default=False)

    def __str__(self):
        return self.user.username


class LikesCount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    userlikes = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
