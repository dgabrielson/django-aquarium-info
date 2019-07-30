# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FishBreedingType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='last modification time')),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField(unique=True, max_length=64)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FishTankRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='last modification time')),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField(unique=True, max_length=64)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FishTemperament',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='last modification time')),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField(unique=True, max_length=64)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FreshwaterFish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='last modification time')),
                ('common_name', models.CharField(max_length=64)),
                ('slug', models.SlugField(unique=True, max_length=64)),
                ('scientific_name', models.CharField(max_length=128, blank=True)),
                ('size_min', models.PositiveSmallIntegerField(help_text='in centimeters (cm)', null=True, verbose_name='minimum size', blank=True)),
                ('size_max', models.PositiveSmallIntegerField(help_text='in centimeters (cm)', null=True, verbose_name='maximum size', blank=True)),
                ('ph_min', models.FloatField(null=True, verbose_name='minimum pH', blank=True)),
                ('ph_max', models.FloatField(null=True, verbose_name='maximum pH', blank=True)),
                ('temperature_min', models.PositiveSmallIntegerField(help_text='in degrees Celcius', null=True, verbose_name='minimum temperature', blank=True)),
                ('temperature_max', models.PositiveSmallIntegerField(help_text='in degrees Celcius', null=True, verbose_name='maximum temperature', blank=True)),
                ('hardness_min', models.PositiveSmallIntegerField(help_text='in parts per million (ppm)', null=True, verbose_name='minimum hardness', blank=True)),
                ('hardness_max', models.PositiveSmallIntegerField(help_text='in parts per million (ppm)', null=True, verbose_name='maximum hardness', blank=True)),
                ('breeding_type', models.ForeignKey(blank=True, to='aquainfo.FishBreedingType', null=True, on_delete=models.SET_NULL)),
            ],
            options={
                'ordering': ('common_name',),
                'verbose_name_plural': 'freshwater fish',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FreshwaterPlant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='last modification time')),
                ('common_name', models.CharField(max_length=64)),
                ('slug', models.SlugField(unique=True, max_length=64)),
                ('scientific_name', models.CharField(max_length=128, blank=True)),
                ('size_min', models.PositiveSmallIntegerField(help_text='in centimeters (cm)', null=True, verbose_name='minimum size', blank=True)),
                ('size_max', models.PositiveSmallIntegerField(help_text='in centimeters (cm)', null=True, verbose_name='maximum size', blank=True)),
                ('ph_min', models.FloatField(null=True, verbose_name='minimum pH', blank=True)),
                ('ph_max', models.FloatField(null=True, verbose_name='maximum pH', blank=True)),
                ('temperature_min', models.PositiveSmallIntegerField(help_text='in degrees Celcius', null=True, verbose_name='minimum temperature', blank=True)),
                ('temperature_max', models.PositiveSmallIntegerField(help_text='in degrees Celcius', null=True, verbose_name='maximum temperature', blank=True)),
                ('hardness_min', models.PositiveSmallIntegerField(help_text='in parts per million (ppm)', null=True, verbose_name='minimum hardness', blank=True)),
                ('hardness_max', models.PositiveSmallIntegerField(help_text='in parts per million (ppm)', null=True, verbose_name='maximum hardness', blank=True)),
            ],
            options={
                'ordering': ('common_name',),
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='last modification time')),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField(unique=True, max_length=64)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlantGrowthSpeed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='last modification time')),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField(unique=True, max_length=64)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlantLighting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='last modification time')),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField(unique=True, max_length=64)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'plant lighting',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlantPropagationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='last modification time')),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField(unique=True, max_length=64)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlantSubstrate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='last modification time')),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField(unique=True, max_length=64)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlantTankRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='last modification time')),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField(unique=True, max_length=64)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='freshwaterplant',
            name='growth_speed',
            field=models.ForeignKey(blank=True, to='aquainfo.PlantGrowthSpeed', null=True, on_delete=models.SET_NULL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='freshwaterplant',
            name='lighting',
            field=models.ForeignKey(blank=True, to='aquainfo.PlantLighting', null=True, on_delete=models.SET_NULL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='freshwaterplant',
            name='origin',
            field=models.ForeignKey(blank=True, to='aquainfo.Origin', null=True, on_delete=models.SET_NULL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='freshwaterplant',
            name='placement',
            field=models.ForeignKey(blank=True, to='aquainfo.PlantTankRegion', null=True, on_delete=models.SET_NULL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='freshwaterplant',
            name='propagation',
            field=models.ForeignKey(blank=True, to='aquainfo.PlantPropagationType', null=True, on_delete=models.SET_NULL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='freshwaterplant',
            name='substrate',
            field=models.ForeignKey(blank=True, to='aquainfo.PlantSubstrate', null=True, on_delete=models.SET_NULL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='freshwaterfish',
            name='origin',
            field=models.ForeignKey(blank=True, to='aquainfo.Origin', null=True, on_delete=models.SET_NULL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='freshwaterfish',
            name='preferred_area',
            field=models.ForeignKey(blank=True, to='aquainfo.FishTankRegion', null=True, on_delete=models.SET_NULL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='freshwaterfish',
            name='temperament_family',
            field=models.ForeignKey(related_name='fishtemperament_family_set', blank=True, to='aquainfo.FishTemperament', null=True, on_delete=models.SET_NULL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='freshwaterfish',
            name='temperament_others',
            field=models.ForeignKey(related_name='fishtemperament_others_set', blank=True, to='aquainfo.FishTemperament', null=True, on_delete=models.SET_NULL),
            preserve_default=True,
        ),
    ]
