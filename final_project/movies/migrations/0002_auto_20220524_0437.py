# Generated by Django 3.2.11 on 2022-05-24 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
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
