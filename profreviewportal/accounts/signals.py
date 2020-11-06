from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.db import models
import datetime
# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import LikesCount, Block


@receiver(user_signed_up)
def after_user_signed_up(user, **kwargs):

    obj = LikesCount.objects.create(user=user, userlikes=0)
    obj2 = Block.objects.create(
        user=user, blockperm=False, tempban=False, end=None)
