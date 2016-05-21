# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_person_todo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='person',
        ),
        migrations.DeleteModel(
            name='todo',
        ),
    ]
