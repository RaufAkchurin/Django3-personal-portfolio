# Generated by Django 3.2.8 on 2022-06-05 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateField(default='1990-12-11'),
        ),
    ]
