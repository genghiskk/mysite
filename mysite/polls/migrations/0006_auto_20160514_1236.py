# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_person_todo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='person_Addr1',
            field=models.CharField(max_length=40, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='person_Addr2',
            field=models.CharField(max_length=40, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='person_City',
            field=models.CharField(max_length=25, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='person_Phone',
            field=models.CharField(max_length=12, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='person_State',
            field=models.CharField(max_length=2, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='person_Zip',
            field=models.CharField(max_length=5, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='todo_updatetext',
            field=models.CharField(max_length=256, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='todoassign_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='todocomplete_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='todoupdate_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
