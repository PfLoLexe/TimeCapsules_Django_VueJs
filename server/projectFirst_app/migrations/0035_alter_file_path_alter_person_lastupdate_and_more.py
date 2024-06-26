# Generated by Django 4.2.7 on 2023-12-04 17:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectFirst_app', '0034_alter_person_lastupdate_alter_person_last_login_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='path',
            field=models.CharField(max_length=4000),
        ),
        migrations.AlterField(
            model_name='person',
            name='lastUpdate',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 12, 4, 17, 35, 2, 125948, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_login',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 12, 4, 17, 35, 2, 125948, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vault',
            name='cDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 4, 17, 35, 2, 127938, tzinfo=datetime.timezone.utc)),
        ),
    ]
