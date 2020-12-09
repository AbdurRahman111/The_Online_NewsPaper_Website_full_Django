# Generated by Django 3.1.4 on 2020-12-03 15:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0010_auto_20201203_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_news_new',
            name='publish',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 3, 21, 47, 35, 444333)),
        ),
        migrations.AlterField(
            model_name='news_comment',
            name='time_comment',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 3, 21, 47, 35, 446331)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='', null=True, upload_to='uploads'),
        ),
    ]