# Generated by Django 3.1.6 on 2021-05-13 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0002_auto_20210430_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='session_key',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
