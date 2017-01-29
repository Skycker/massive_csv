# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-01-26 22:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.EmailField(max_length=254)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='web_site.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=32)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='web_site.Customer')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='phone',
            unique_together=set([('customer', 'number')]),
        ),
        migrations.AlterUniqueTogether(
            name='email',
            unique_together=set([('customer', 'address')]),
        ),
    ]
