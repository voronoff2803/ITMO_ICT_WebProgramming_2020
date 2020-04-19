# Generated by Django 3.0.5 on 2020-04-19 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raceapp', '0002_auto_20200419_0832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='result',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='raceapp.Result', verbose_name='Результат'),
        ),
    ]