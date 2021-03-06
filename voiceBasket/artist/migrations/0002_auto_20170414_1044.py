# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 10:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20170414_0733'),
        ('artist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artistrequest',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.GenericUser'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='request',
            name='additional_notes',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='audio_book_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='duration_in_minutes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='ivr_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='reference_file_url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='script_text',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='script_url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='word_count',
            field=models.IntegerField(null=True),
        ),
    ]
