# Generated by Django 4.2.7 on 2023-12-03 16:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectFirst_app', '0026_comments_vault_alter_person_lastupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='commentDate',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='lastUpdate',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 12, 3, 16, 21, 5, 287513, tzinfo=datetime.timezone.utc)),
        ),
    ]
