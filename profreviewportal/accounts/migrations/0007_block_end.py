# Generated by Django 3.0.4 on 2020-03-30 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_block_datetillblock'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='end',
            field=models.DateTimeField(null=True),
        ),
    ]
