# Generated by Django 3.1.7 on 2023-05-03 08:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20230503_0040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='bmi',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='color',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.color'),
        ),
        migrations.AddField(
            model_name='customer',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 3, 16, 3, 10, 938427), null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.gender'),
        ),
    ]