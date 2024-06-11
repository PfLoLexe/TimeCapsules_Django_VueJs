# Generated by Django 4.2.7 on 2023-12-03 16:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectFirst_app', '0021_alter_person_lastupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='vault',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectFirst_app.vault'),
        ),
        migrations.AlterField(
            model_name='person',
            name='lastUpdate',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 12, 3, 16, 10, 28, 56304, tzinfo=datetime.timezone.utc)),
        ),
    ]
