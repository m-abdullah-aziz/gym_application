# Generated by Django 4.1.1 on 2022-10-03 01:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('athlete', '0008_remove_athleteexercise_times_athleteexercise_athlete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athleteexercise',
            name='athlete',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='athlete', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='athleteexercise',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercise', to='exercise.exercise'),
        ),
    ]
