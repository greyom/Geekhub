# Generated by Django 3.2.11 on 2022-06-14 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='info',
            field=models.TextField(blank=True),
        ),
    ]
