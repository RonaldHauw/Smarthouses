# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.House')),
            ],
        ),
        migrations.AddField(
            model_name='house',
            name='demo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.Neighbourhood'),
        ),
    ]
