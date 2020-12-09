# Generated by Django 3.1.4 on 2020-12-03 05:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsApp', '0003_auto_20201203_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_news',
            name='publish',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 3, 11, 32, 44, 236102)),
        ),
        migrations.AlterField(
            model_name='news_comment',
            name='time_comment',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 3, 11, 32, 44, 239099)),
        ),
        migrations.AlterField(
            model_name='news_comment_new',
            name='time_comment',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 3, 11, 32, 44, 239099)),
        ),
        migrations.CreateModel(
            name='add_news_new',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_news', models.CharField(max_length=300)),
                ('image', models.ImageField(default='', upload_to='uploads')),
                ('slug', models.CharField(max_length=130)),
                ('Repoter_name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('publish', models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 3, 11, 32, 44, 237101))),
                ('catagory', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='newsApp.catagory_of_news')),
                ('likes', models.ManyToManyField(related_name='news_post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]