# Generated by Django 3.1.5 on 2021-02-01 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_gusto', '0004_banners'),
    ]

    operations = [
        migrations.AddField(
            model_name='banners',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
    ]
