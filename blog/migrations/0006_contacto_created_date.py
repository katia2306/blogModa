# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
