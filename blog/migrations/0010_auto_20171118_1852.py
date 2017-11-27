# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tips',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
                ('tipo', models.CharField(max_length=20)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='tipo',
            field=models.CharField(max_length=20),
        ),
    ]
