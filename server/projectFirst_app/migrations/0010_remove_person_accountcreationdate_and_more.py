# Generated by Django 4.2.7 on 2023-12-02 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectFirst_app', '0009_alter_person_accountcreationdate_alter_person_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='accountCreationDate',
        ),
        migrations.RemoveField(
            model_name='person',
            name='fullName',
        ),
        migrations.AlterField(
            model_name='person',
            name='lastUpdate',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 12, 2, 12, 26, 30, 775103, tzinfo=datetime.timezone.utc)),
        ),
    ]
