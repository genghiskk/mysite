# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20160514_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('person_id', models.IntegerField(default=0)),
                ('person_FName', models.CharField(max_length=25)),
                ('person_LName', models.CharField(max_length=25)),
                ('person_role', models.CharField(max_length=10)),
                ('person_Phone', models.CharField(max_length=12, blank=True)),
                ('person_Addr1', models.CharField(max_length=40, blank=True)),
                ('person_Addr2', models.CharField(max_length=40, blank=True)),
                ('person_City', models.CharField(max_length=25, blank=True)),
                ('person_State', models.CharField(max_length=2, blank=True)),
                ('person_Zip', models.CharField(max_length=5, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('todo_id', models.IntegerField(default=0)),
                ('todo_desc', models.CharField(max_length=256)),
                ('todo_updatetext', models.CharField(max_length=256, blank=True)),
                ('todo_type', models.CharField(max_length=15)),
                ('todo_assignee', models.IntegerField(default=0)),
                ('todo_assigner', models.IntegerField(default=0)),
                ('todoassign_date', models.DateTimeField(blank=True)),
                ('todoupdate_date', models.DateTimeField(blank=True)),
                ('todocomplete_date', models.DateTimeField(blank=True)),
            ],
        ),
    ]
