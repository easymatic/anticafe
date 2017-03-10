# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-10 11:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indentifier', models.TextField()),
                ('plan', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='plan.Plan')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(null=True)),
                ('second_name', models.TextField(null=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.Card')),
            ],
        ),
    ]
