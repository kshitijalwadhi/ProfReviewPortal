from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.db import models
import datetime
# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Block(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    BOOL_CHOICES = ((False, 'No'), (True, 'Yes'))
    blockperm = models.BooleanField(choices=BOOL_CHOICES, default=False)
    tempban = models.BooleanField(choices=BOOL_CHOICES, default=False)
    end = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.username


class LikesCount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    userlikes = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


@receiver(user_signed_up)
def after_user_signed_up(user, **kwargs):

    obj = LikesCount.objects.create(user=user, userlikes=0)
    obj2 = Block.objects.create(
        user=user, blockperm=False, tempban=False, end=None)
