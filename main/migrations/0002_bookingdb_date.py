# Generated by Django 3.2 on 2022-02-27 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingdb',
            name='date',
            field=models.DateField(default=None),
        ),
    ]
