# Generated by Django 3.1.7 on 2023-04-30 12:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20230430_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date',
        ),
        migrations.AddField(
            model_name='order',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 30, 20, 38, 45, 710192), null=True),
        ),
    ]
