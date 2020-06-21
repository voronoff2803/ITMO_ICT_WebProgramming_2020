# Generated by Django 3.0.5 on 2020-06-18 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0002_person_vehicles'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalData',
            fields=[
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='project_first_app.Person')),
                ('passport_num', models.CharField(max_length=128)),
                ('home_address', models.CharField(max_length=128)),
                ('nationality', models.CharField(max_length=128)),
            ],
        ),
    ]
