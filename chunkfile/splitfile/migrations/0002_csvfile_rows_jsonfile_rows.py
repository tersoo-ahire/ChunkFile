# Generated by Django 4.0.6 on 2022-07-24 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splitfile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='csvfile',
            name='rows',
            field=models.PositiveIntegerField(default=100),
        ),
        migrations.AddField(
            model_name='jsonfile',
            name='rows',
            field=models.PositiveIntegerField(default=100),
        ),
    ]