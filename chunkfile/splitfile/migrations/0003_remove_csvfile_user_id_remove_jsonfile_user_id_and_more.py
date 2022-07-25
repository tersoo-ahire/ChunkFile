# Generated by Django 4.0.6 on 2022-07-24 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('splitfile', '0002_csvfile_rows_jsonfile_rows'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csvfile',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='jsonfile',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='splitfile.signin'),
        ),
        migrations.AlterField(
            model_name='jsonfile',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='splitfile.signin'),
        ),
    ]