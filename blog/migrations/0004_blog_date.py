# Generated by Django 3.2.8 on 2022-06-06 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220606_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateField(default='1990-10-18'),
        ),
    ]
