# Generated by Django 3.1.6 on 2021-05-13 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('_auth', '0005_auto_20210513_2345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='avatar',
        ),
    ]