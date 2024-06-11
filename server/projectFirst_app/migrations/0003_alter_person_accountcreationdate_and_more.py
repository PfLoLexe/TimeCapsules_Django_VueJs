# Generated by Django 4.2.7 on 2023-12-02 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectFirst_app', '0002_alter_person_birthdate_alter_person_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='accountCreationDate',
            field=models.DateField(blank=True, default=datetime.date(2023, 12, 2)),
        ),
        migrations.AlterField(
            model_name='person',
            name='capCount',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, default='example@notset.com', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='lastUpdate',
            field=models.DateField(blank=True, default=datetime.date(2023, 12, 2)),
        ),
    ]
