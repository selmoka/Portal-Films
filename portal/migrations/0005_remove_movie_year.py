# Generated by Django 2.2 on 2019-04-10 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_movie_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='year',
        ),
    ]
