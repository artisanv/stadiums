# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160426_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game_result',
            name='loser',
            field=models.CharField(max_length=255, verbose_name=b'loser'),
        ),
    ]
