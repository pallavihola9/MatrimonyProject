# Generated by Django 4.2.6 on 2023-11-06 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapi', '0003_alter_profile_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.CharField(default='2023-11-06', max_length=10),
        ),
    ]
