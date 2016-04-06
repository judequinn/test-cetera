# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20160406_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='of_type',
        ),
        migrations.AddField(
            model_name='response',
            name='of_type',
            field=models.ManyToManyField(to='testapp.Type'),
        ),
    ]
