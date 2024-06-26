# Generated by Django 4.2.7 on 2023-12-02 15:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectFirst_app', '0014_alter_comments_maincomment_alter_person_lastupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='mainComment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='set_main_comment', to='projectFirst_app.comments'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='subComments',
            field=models.ManyToManyField(blank=True, to='projectFirst_app.comments'),
        ),
        migrations.AlterField(
            model_name='person',
            name='lastUpdate',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 12, 2, 15, 19, 8, 550646, tzinfo=datetime.timezone.utc)),
        ),
    ]
