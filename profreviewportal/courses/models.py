from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


# class Course(models.Model):
#     code = models.CharField(max_length=10)
#     comment = models.TextField()
#     difficulty = models.IntegerField(
#         default=1,
#         validators=[MaxValueValidator(10), MinValueValidator(1)]
#     )
#     contentquality = models.IntegerField(
#         default=1,
#         validators=[MaxValueValidator(10), MinValueValidator(1)]
#     )

#     def __str__(self):
#         return self.code


# class Prof(models.Model):
#     prof = models.ForeignKey(Course, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100, default='')

#     def __str__(self):
#         return self.prof
