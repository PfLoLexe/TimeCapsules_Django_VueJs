# Generated by Django 4.2.7 on 2023-12-04 15:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectFirst_app', '0029_alter_person_lastupdate_alter_person_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='lastUpdate',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 12, 4, 15, 59, 55, 94370, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_login',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 12, 4, 15, 59, 55, 95366, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vault',
            name='cDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 4, 15, 59, 55, 96363, tzinfo=datetime.timezone.utc)),
        ),
    ]
