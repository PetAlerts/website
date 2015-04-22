# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=1, choices=[(b'D', 'Dog'), (b'C', 'Cat'), (b'O', 'Other')])),
                ('age', models.CharField(blank=True, max_length=2, null=True, choices=[(b'CU', 'Cub'), (b'AD', 'Adult')])),
                ('health', models.CharField(blank=True, max_length=1, null=True, choices=[(b'G', 'Good'), (b'B', 'Bad')])),
                ('picture', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.AddField(
            model_name='alert',
            name='animal',
            field=models.ForeignKey(to='pets.Animal'),
        ),
    ]
