# Generated by Django 4.2.7 on 2023-12-04 13:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectFirst_app', '0028_alter_person_lastupdate_alter_person_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='lastUpdate',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 12, 4, 13, 16, 29, 987807, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_login',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 12, 4, 13, 16, 29, 987807, tzinfo=datetime.timezone.utc)),
        ),
    ]
