# Generated by Django 3.0.3 on 2020-06-26 06:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_roll', models.IntegerField(default=100)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(default='ques.png', upload_to='student_profile')),
                ('age', models.IntegerField(default=0)),
                ('dob', models.DateField(verbose_name=datetime.datetime.today)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('about', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('joining_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('address', models.TextField()),
                ('mobile', models.CharField(default='', max_length=12)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
