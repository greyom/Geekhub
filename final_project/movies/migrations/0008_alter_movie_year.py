# Generated by Django 3.2.11 on 2022-05-25 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20220525_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.TextField(blank=True),
        ),
    ]
