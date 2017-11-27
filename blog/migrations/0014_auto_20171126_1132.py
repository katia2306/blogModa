# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20171126_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commenttips',
            name='post',
        ),
        migrations.DeleteModel(
            name='CommentTips',
        ),
        migrations.DeleteModel(
            name='Tips',
        ),
    ]
