from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Prof(models.Model):
    profname = models.CharField(max_length=100)

    def __str__(self):
        return self.profname


class Course(models.Model):
    courseName = models.CharField(max_length=50)

    def __str__(self):
        return self.courseName


class Review(models.Model):
    code = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    prof = models.ForeignKey(Prof, on_delete=models.CASCADE, null=True)
    comment = models.TextField()
    difficulty = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    contentquality = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    BOOL_CHOICES = ((False, 'No'), (True, 'Yes'))
    anonymous = models.BooleanField(choices=BOOL_CHOICES, default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField(auto_now_add=True)
    report = models.BooleanField(
        choices=BOOL_CHOICES, default=False, null=True)

    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    dislikes = models.ManyToManyField(
        User, related_name="dislikes", blank=True)


class Warning(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)
