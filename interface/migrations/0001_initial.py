# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_created=True)),
                ('sid', models.CharField(max_length=64)),
                ('status', models.CharField(max_length=12)),
                ('from_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, blank=True)),
                ('to_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Greeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_created=True)),
                ('active', models.BooleanField(default=True)),
                ('audio_file_link', models.URLField()),
                ('originating_call', models.ForeignKey(to='interface.Call')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_created=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VoiceMail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_created=True)),
                ('audio_file_link', models.URLField()),
                ('originating_call', models.ForeignKey(to='interface.Call')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='greeting',
            name='phone_number',
            field=models.ForeignKey(to='interface.PhoneNumber'),
            preserve_default=True,
        ),
    ]
