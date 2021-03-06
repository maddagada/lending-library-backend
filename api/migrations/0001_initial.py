# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-05 19:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicanttype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Areaofinterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('description', models.TextField(blank=True)),
                ('awardlink', models.URLField(max_length=1000)),
                ('sponsororg', models.CharField(blank=True, max_length=1000)),
                ('recurring', models.BooleanField(default=False)),
                ('nomreq', models.BooleanField(default=False)),
                ('recurinterval', models.CharField(blank=True, max_length=1000)),
                ('opendate', models.DateTimeField()),
                ('nomdeadline', models.DateTimeField()),
                ('submdeadline', models.DateTimeField()),
                ('additionalinfo', models.TextField(blank=True)),
                ('previousapplicants', models.IntegerField(default=0)),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('applicanttypes', models.ManyToManyField(blank=True, related_name='awards', to='api.Applicanttype')),
            ],
        ),
        migrations.CreateModel(
            name='Awardpurpose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org', models.CharField(choices=[('unl', 'University of Nebraska - Lincoln'), ('uno', 'University of Nebraska - Omaha'), ('unmc', 'University of Nebraska Medical Center'), ('unk', 'University of Nebraska - Kearney'), ('other', 'Other')], default='uno', max_length=30)),
                ('college', models.CharField(blank=True, max_length=1000)),
                ('dept', models.CharField(blank=True, max_length=1000)),
                ('otherdetails', models.CharField(blank=True, max_length=1000)),
                ('areasofinterest', models.ManyToManyField(blank=True, related_name='profiles', to='api.Areaofinterest')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('federal', 'Federal Government'), ('state', 'State Government'), ('local', 'Local Government'), ('internal', 'Internal'), ('private_industry', 'Private Industry'), ('other', 'Other')], default='other', max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stemfield',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='award',
            name='awardpurposes',
            field=models.ManyToManyField(blank=True, related_name='awards', to='api.Awardpurpose'),
        ),
        migrations.AddField(
            model_name='award',
            name='createdby',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='awards', to='api.Profile'),
        ),
        migrations.AddField(
            model_name='award',
            name='source',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='awards', to='api.Source'),
        ),
        migrations.AddField(
            model_name='award',
            name='stemfields',
            field=models.ManyToManyField(blank=True, related_name='awards', to='api.Stemfield'),
        ),
    ]
