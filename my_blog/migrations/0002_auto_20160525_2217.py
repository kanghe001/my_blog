# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-id'], 'verbose_name': '\u7528\u6237', 'verbose_name_plural': '\u7528\u6237'},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='artical',
            field=models.ForeignKey(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0', blank=True, to='my_blog.Artical', null=True),
        ),
        migrations.AlterField(
            model_name='artical',
            name='tag',
            field=models.ManyToManyField(to='my_blog.Tag', verbose_name='\u6807\u7b7e'),
        ),
    ]
