# Generated by Django 4.0.2 on 2022-04-04 17:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_cast_bio_cast_birthday_cast_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cast',
            name='birthday',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 4, 13, 3, 43, 138804)),
        ),
    ]
