# Generated by Django 4.1.1 on 2022-10-03 18:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athlete', '0011_alter_athleteexercise_exercise_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athleteexercise',
            name='exercise_date',
            field=models.DateField(default=datetime.date(2022, 10, 3)),
        ),
    ]
