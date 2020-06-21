# Generated by Django 3.0.5 on 2020-04-19 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Вопрос о сотрудничестве'), (2, 'Вопрос о гонках'), (3, 'Иное')], default=3)),
                ('text', models.CharField(max_length=100, verbose_name='Описание')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('description', models.CharField(max_length=100, verbose_name='Описание')),
                ('team', models.CharField(max_length=100, verbose_name='Название команды')),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E')], default=1)),
                ('experience', models.FloatField(max_length=100, verbose_name='Опыт')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.CharField(max_length=100, verbose_name='Описание')),
                ('volume', models.FloatField(max_length=100, verbose_name='Объем мотора')),
                ('hp', models.FloatField(max_length=100, verbose_name='Лошадиные силы')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.CharField(max_length=100, verbose_name='Описание')),
                ('date', models.DateField(verbose_name='Дата')),
                ('result', models.DurationField(verbose_name='Время заезда')),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raceapp.Comment', verbose_name='Комментарии')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raceapp.Person', verbose_name='Пилот')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raceapp.Vehicle', verbose_name='Автомобиль')),
            ],
        ),
    ]