# Generated by Django 4.2.7 on 2023-12-03 16:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectFirst_app', '0019_alter_person_lastupdate_alter_vaultaccess_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='vault',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='projectFirst_app.vault'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='lastUpdate',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 12, 3, 16, 4, 44, 43067, tzinfo=datetime.timezone.utc)),
        ),
    ]