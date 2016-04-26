# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='day',
            field=models.CharField(default=b'SUNDAY', max_length=100, choices=[(b'SATURDAY', b'Saturday'), (b'SUNDAY', b'Sunday'), (b'MONDAY', b'Monday'), (b'TUESDAY', b'Tuesday'), (b'WEDNSDAY', b'Wednsday'), (b'THURSDAY', b'Friday')]),
        ),
    ]
