# Generated by Django 3.0.3 on 2020-06-26 09:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='dob',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]