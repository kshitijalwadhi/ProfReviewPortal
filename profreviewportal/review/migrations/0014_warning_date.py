# Generated by Django 3.0.4 on 2020-03-27 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0013_warning'),
    ]

    operations = [
        migrations.AddField(
            model_name='warning',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
