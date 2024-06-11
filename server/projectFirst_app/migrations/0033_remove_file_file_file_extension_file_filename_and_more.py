# Generated by Django 4.2.7 on 2023-12-04 17:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectFirst_app', '0032_alter_person_lastupdate_alter_person_last_login_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='file',
        ),
        migrations.AddField(
            model_name='file',
            name='extension',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='filename',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='lastUpdate',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 12, 4, 17, 33, 44, 49658, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_login',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 12, 4, 17, 33, 44, 49658, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vault',
            name='cDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 4, 17, 33, 44, 51651, tzinfo=datetime.timezone.utc)),
        ),
    ]