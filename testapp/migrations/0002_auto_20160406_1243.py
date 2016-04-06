# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='of_type',
        ),
        migrations.AddField(
            model_name='response',
            name='of_type',
            field=models.ForeignKey(default=1, to='testapp.Type'),
            preserve_default=False,
        ),
    ]
