from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Prof(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    courseName = models.CharField(max_length=50)

    def __str__(self):
        return self.courseName


class Review(models.Model):
    code = models.OneToOneField(
        Course, on_delete=models.CASCADE, null=True)
    prof = models.OneToOneField(Prof, on_delete=models.CASCADE, null=True)
    comment = models.TextField()
    difficulty = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    contentquality = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    # def __str__(self):
    #     return self.code
