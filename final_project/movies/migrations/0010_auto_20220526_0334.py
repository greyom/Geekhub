# Generated by Django 3.2.11 on 2022-05-26 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_alter_movie_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='category',
        ),
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.ManyToManyField(related_name='movies', to='movies.Category'),
        ),
    ]
