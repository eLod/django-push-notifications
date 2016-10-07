# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('push_notifications', '0003_wnsdevice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apnsdevice',
            name='registration_id',
            field=models.CharField(verbose_name='Registration ID', max_length=200),
        ),
        migrations.AlterUniqueTogether(
            name='apnsdevice',
            unique_together=set([('registration_id', 'user')]),
        ),
    ]
