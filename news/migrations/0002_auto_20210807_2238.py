# Generated by Django 3.2.6 on 2021-08-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headline',
            name='image',
        ),
        migrations.AddField(
            model_name='headline',
            name='text',
            field=models.CharField(default='No content', max_length=100000000000000000000000),
        ),
    ]
