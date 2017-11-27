# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20171112_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tipo',
            field=models.CharField(default=[('Trendy', 'trendy'), ('Tips', 'tips')], max_length=20),
        ),
    ]
