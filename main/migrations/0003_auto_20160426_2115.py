# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_game_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game_result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('result', models.SlugField()),
                ('winner', models.CharField(max_length=255, verbose_name=b'winner')),
                ('winner_image', models.ImageField(upload_to=b'')),
                ('loser', models.CharField(max_length=255, verbose_name=b'winner')),
                ('loser_image', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='rank',
            field=models.FloatField(default=0.0),
        ),
    ]
