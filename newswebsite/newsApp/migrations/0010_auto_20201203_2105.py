# Generated by Django 3.1.4 on 2020-12-03 15:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsApp', '0009_auto_20201203_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_news_new',
            name='publish',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 3, 21, 5, 6, 315347)),
        ),
        migrations.AlterField(
            model_name='news_comment',
            name='time_comment',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 3, 21, 5, 6, 317346)),
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_name', models.CharField(max_length=255, null=True)),
                ('profile_email', models.CharField(max_length=255, null=True)),
                ('profile_phone', models.CharField(max_length=255, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
