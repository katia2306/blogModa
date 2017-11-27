# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_commenttips'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tipo',
            field=models.CharField(max_length=20, choices=[('Trendy', 'trendy'), ('Tips', 'tips')]),
        ),
    ]
