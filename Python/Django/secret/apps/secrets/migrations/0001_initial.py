# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('likes', models.ManyToManyField(related_name='likes', to='loginApp.User')),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='loginApp.User')),
            ],
        ),
    ]
