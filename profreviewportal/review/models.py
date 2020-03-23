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
    code = models.ManyToManyField(Course)
    prof = models.ManyToManyField(Prof)
    comment = models.TextField()
    difficulty = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    contentquality = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )

    # def __str__(self):
    #     return self.code
