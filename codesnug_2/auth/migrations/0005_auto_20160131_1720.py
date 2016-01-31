# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codesnug_2_auth', '0004_auto_20160131_1720'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='codesnugusergroup',
            options={'ordering': ('created_at',)},
        ),
        migrations.AlterUniqueTogether(
            name='codesnugusergroup',
            unique_together=set([('title', 'owner')]),
        ),
    ]
