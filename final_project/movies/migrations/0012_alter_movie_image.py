# Generated by Django 3.2.11 on 2022-06-12 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_alter_movie_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, default='no_image.png', upload_to='movies/'),
        ),
    ]
