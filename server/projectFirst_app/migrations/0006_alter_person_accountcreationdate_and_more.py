# Generated by Django 4.2.7 on 2023-12-02 12:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectFirst_app', '0005_alter_person_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='accountCreationDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 2, 12, 9, 18, 492705, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='person',
            name='lastUpdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 2, 12, 9, 18, 492705, tzinfo=datetime.timezone.utc)),
        ),
    ]
