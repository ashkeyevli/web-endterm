# Generated by Django 3.1.6 on 2021-05-14 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0010_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='review.review', verbose_name='Отзыв'),
        ),
    ]