# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='workspace',
            name='owner',
            field=models.ForeignKey(related_name='owned_workspaces', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='workspace',
            unique_together=set([('title', 'owner')]),
        ),
    ]
