# Generated by Django 3.1.3 on 2020-11-26 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='temperature',
            field=models.FloatField(),
        ),
    ]
