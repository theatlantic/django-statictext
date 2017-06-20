# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statictext', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statictext',
            name='kicker',
            field=models.CharField(default=b'', max_length=50, blank=True),
        ),
    ]
