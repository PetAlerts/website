# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaSubscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lat', models.FloatField(validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)])),
                ('lng', models.FloatField(validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)])),
                ('radius_km', models.PositiveIntegerField(help_text='Maximum distance from location in Km. (1 to 7)', validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(7)])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
