# Generated by Django 3.1.4 on 2020-12-03 06:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0004_auto_20201203_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_news_new',
            name='publish',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 3, 12, 19, 58, 891137)),
        ),
        migrations.AlterField(
            model_name='news_comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsApp.add_news_new'),
        ),
        migrations.AlterField(
            model_name='news_comment',
            name='time_comment',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 3, 12, 19, 58, 892135)),
        ),
        migrations.AlterField(
            model_name='news_comment_new',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsApp.add_news_new'),
        ),
        migrations.AlterField(
            model_name='news_comment_new',
            name='time_comment',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 3, 12, 19, 58, 893135)),
        ),
        migrations.DeleteModel(
            name='add_news',
        ),
    ]
