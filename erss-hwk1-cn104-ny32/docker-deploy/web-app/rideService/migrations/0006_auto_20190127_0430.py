# Generated by Django 2.1.5 on 2019-01-27 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideService', '0005_auto_20190127_0423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver',
            old_name='user_name',
            new_name='account',
        ),
    ]