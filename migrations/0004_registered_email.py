# Generated by Django 3.1.4 on 2020-12-27 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201227_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='registered',
            name='email',
            field=models.EmailField(blank=True, max_length=30),
        ),
    ]
