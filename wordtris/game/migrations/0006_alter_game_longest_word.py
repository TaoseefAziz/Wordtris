# Generated by Django 4.2.1 on 2023-05-07 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_alter_game_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='longest_word',
            field=models.CharField(blank=True, max_length=10, null='True'),
        ),
    ]
