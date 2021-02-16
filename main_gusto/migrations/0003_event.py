# Generated by Django 3.1.5 on 2021-02-01 17:09

from django.db import migrations, models
import main_gusto.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_gusto', '0002_dish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to=main_gusto.models.Event.get_file_name_events)),
                ('description', models.TextField(null=True)),
                ('event_date', models.DateField()),
                ('event_time', models.TimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
