# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0002_auto_20160525_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artical',
            name='date_publish',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4', null=True),
        ),
    ]
