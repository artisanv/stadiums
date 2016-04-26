# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160426_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='game_result',
            name='game',
            field=models.ForeignKey(default=True, to='main.Game'),
        ),
    ]
