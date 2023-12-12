# Generated by Django 4.2.6 on 2023-11-02 05:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='auth_provider',
            field=models.CharField(default='email', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='phoneNumber',
            field=models.CharField(default=False, max_length=2322),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.CharField(default=datetime.date.today, max_length=150),
        ),
    ]
