# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('codesnug_2_auth', '0002_codesnugusergroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='codesnugusergroup',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='codesnugusergroup',
            name='owner',
            field=models.ForeignKey(related_name='owned_groups', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
