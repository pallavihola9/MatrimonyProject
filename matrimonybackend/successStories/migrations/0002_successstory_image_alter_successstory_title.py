# Generated by Django 4.2.6 on 2024-01-11 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('successStories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='successstory',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='success_stories'),
        ),
        migrations.AlterField(
            model_name='successstory',
            name='Title',
            field=models.CharField(blank=True, default=None, max_length=222222222, null=True),
        ),
    ]