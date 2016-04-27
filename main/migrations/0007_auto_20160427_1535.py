# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_game_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game_result',
            name='loser_image',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='game_result',
            name='winner_image',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
