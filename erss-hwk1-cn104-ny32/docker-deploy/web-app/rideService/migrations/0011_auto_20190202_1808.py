# Generated by Django 2.1.5 on 2019-02-02 18:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideService', '0010_auto_20190202_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sharer',
            name='account',
        ),
        migrations.RemoveField(
            model_name='request',
            name='confirmed',
        ),
        migrations.AddField(
            model_name='request',
            name='num_sharer',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='request',
            name='vehicle_type',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Sharer',
        ),
    ]
