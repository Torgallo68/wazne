# Generated by Django 5.1.4 on 2025-01-01 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='body',
        ),
        migrations.AddField(
            model_name='note',
            name='name',
            field=models.CharField(default='Brak nazwy', max_length=100),
        ),
        migrations.AddField(
            model_name='note',
            name='reps',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='note',
            name='sets',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='note',
            name='weight',
            field=models.FloatField(default=0.0),
        ),
    ]