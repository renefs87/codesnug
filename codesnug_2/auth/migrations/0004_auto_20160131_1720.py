# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('codesnug_2_auth', '0003_auto_20160131_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='codesnugusergroup',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 31, 17, 20, 31, 608390, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='codesnugusergroup',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True),
        ),
    ]
