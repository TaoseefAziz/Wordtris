# Generated by Django 4.2.1 on 2023-05-05 20:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date_played',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]