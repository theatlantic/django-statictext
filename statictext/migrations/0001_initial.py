# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=False, help_text=b'Display on Site')),
                ('content', models.TextField(max_length=500, blank=True)),
                ('url', models.URLField(verbose_name=b'URL', blank=True)),
                ('slug', models.SlugField()),
                ('layout', models.CharField(default=b'', max_length=100, blank=True)),
                ('site', models.ForeignKey(to='sites.Site')),
            ],
            options={
                'verbose_name': 'Text Snippet',
                'verbose_name_plural': 'Text Snippets',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='statictext',
            unique_together=set([('slug', 'site')]),
        ),
    ]
