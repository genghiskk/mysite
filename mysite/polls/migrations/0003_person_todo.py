# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20160512_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('person_id', models.IntegerField(default=0)),
                ('person_FName', models.CharField(max_length=25)),
                ('person_LName', models.CharField(max_length=25)),
                ('person_role', models.CharField(max_length=10)),
                ('person_Phone', models.CharField(max_length=12)),
                ('person_Addr1', models.CharField(max_length=40)),
                ('person_Addr2', models.CharField(max_length=40)),
                ('person_City', models.CharField(max_length=25)),
                ('person_State', models.CharField(max_length=2)),
                ('person_Zip', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('todo_id', models.IntegerField(default=0)),
                ('todo_desc', models.CharField(max_length=256)),
                ('todo_updatetext', models.CharField(max_length=256)),
                ('todo_type', models.CharField(max_length=15)),
                ('todo_assignee', models.IntegerField(default=0)),
                ('todo_assigner', models.IntegerField(default=0)),
                ('todoassign_date', models.DateTimeField()),
                ('todoupdate_date', models.DateTimeField()),
                ('todocomplete_date', models.DateTimeField()),
            ],
        ),
    ]
