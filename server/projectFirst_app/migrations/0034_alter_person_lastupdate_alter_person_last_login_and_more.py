# Generated by Django 4.2.7 on 2023-12-04 17:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectFirst_app', '0033_remove_file_file_file_extension_file_filename_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='lastUpdate',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 12, 4, 17, 34, 19, 332599, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_login',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 12, 4, 17, 34, 19, 332599, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vault',
            name='cDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 4, 17, 34, 19, 334591, tzinfo=datetime.timezone.utc)),
        ),
    ]
