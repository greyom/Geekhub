# Generated by Django 3.2.11 on 2022-02-01 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ask',
            name='kids',
            field=models.TextField(null=True),
        ),
    ]