# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20171126_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tipo',
            field=models.CharField(default='trendy', choices=[('Trendy', 'trendy'), ('Tips', 'tips')], max_length=20),
        ),
    ]
