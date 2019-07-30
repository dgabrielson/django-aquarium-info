# -*- coding: utf-8 -*-
import datetime

from django.db import models

from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Origin'
        db.create_table('aquainfo_origin', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=64)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('aquainfo', ['Origin'])

        # Adding model 'FishBreedingType'
        db.create_table('aquainfo_fishbreedingtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=64)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('aquainfo', ['FishBreedingType'])

        # Adding model 'PlantPropagationType'
        db.create_table('aquainfo_plantpropagationtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=64)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('aquainfo', ['PlantPropagationType'])

        # Adding model 'PlantTankRegion'
        db.create_table('aquainfo_planttankregion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=64)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('aquainfo', ['PlantTankRegion'])

        # Adding model 'FishTankRegion'
        db.create_table('aquainfo_fishtankregion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=64)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('aquainfo', ['FishTankRegion'])

        # Adding model 'FishTemperament'
        db.create_table('aquainfo_fishtemperament', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=64)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('aquainfo', ['FishTemperament'])

        # Adding model 'PlantGrowthSpeed'
        db.create_table('aquainfo_plantgrowthspeed', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=64)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('aquainfo', ['PlantGrowthSpeed'])

        # Adding model 'PlantLighting'
        db.create_table('aquainfo_plantlighting', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=64)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('aquainfo', ['PlantLighting'])

        # Adding model 'PlantSubstrate'
        db.create_table('aquainfo_plantsubstrate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=64)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('aquainfo', ['PlantSubstrate'])

        # Adding model 'FreshwaterFish'
        db.create_table('aquainfo_freshwaterfish', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('common_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=64)),
            ('scientific_name', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('origin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aquainfo.Origin'], null=True, blank=True)),
            ('size_min', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('size_max', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('ph_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('ph_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('temperature_min', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('temperature_max', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('hardness_min', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('hardness_max', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('breeding_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aquainfo.FishBreedingType'], null=True, blank=True)),
            ('preferred_area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aquainfo.FishTankRegion'], null=True, blank=True)),
            ('temperament_family', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='fishtemperament_family_set', null=True, to=orm['aquainfo.FishTemperament'])),
            ('temperament_others', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='fishtemperament_others_set', null=True, to=orm['aquainfo.FishTemperament'])),
        ))
        db.send_create_signal('aquainfo', ['FreshwaterFish'])

        # Adding model 'FreshwaterPlant'
        db.create_table('aquainfo_freshwaterplant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('common_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=64)),
            ('scientific_name', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('origin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aquainfo.Origin'], null=True, blank=True)),
            ('size_min', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('size_max', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('ph_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('ph_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('temperature_min', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('temperature_max', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('hardness_min', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('hardness_max', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('growth_speed', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aquainfo.PlantGrowthSpeed'], null=True, blank=True)),
            ('lighting', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aquainfo.PlantLighting'], null=True, blank=True)),
            ('placement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aquainfo.PlantTankRegion'], null=True, blank=True)),
            ('propagation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aquainfo.PlantPropagationType'], null=True, blank=True)),
            ('substrate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aquainfo.PlantSubstrate'], null=True, blank=True)),
        ))
        db.send_create_signal('aquainfo', ['FreshwaterPlant'])


    def backwards(self, orm):
        # Deleting model 'Origin'
        db.delete_table('aquainfo_origin')

        # Deleting model 'FishBreedingType'
        db.delete_table('aquainfo_fishbreedingtype')

        # Deleting model 'PlantPropagationType'
        db.delete_table('aquainfo_plantpropagationtype')

        # Deleting model 'PlantTankRegion'
        db.delete_table('aquainfo_planttankregion')

        # Deleting model 'FishTankRegion'
        db.delete_table('aquainfo_fishtankregion')

        # Deleting model 'FishTemperament'
        db.delete_table('aquainfo_fishtemperament')

        # Deleting model 'PlantGrowthSpeed'
        db.delete_table('aquainfo_plantgrowthspeed')

        # Deleting model 'PlantLighting'
        db.delete_table('aquainfo_plantlighting')

        # Deleting model 'PlantSubstrate'
        db.delete_table('aquainfo_plantsubstrate')

        # Deleting model 'FreshwaterFish'
        db.delete_table('aquainfo_freshwaterfish')

        # Deleting model 'FreshwaterPlant'
        db.delete_table('aquainfo_freshwaterplant')


    models = {
        'aquainfo.fishbreedingtype': {
            'Meta': {'object_name': 'FishBreedingType'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '64'})
        },
        'aquainfo.fishtankregion': {
            'Meta': {'object_name': 'FishTankRegion'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '64'})
        },
        'aquainfo.fishtemperament': {
            'Meta': {'object_name': 'FishTemperament'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '64'})
        },
        'aquainfo.freshwaterfish': {
            'Meta': {'ordering': "('common_name',)", 'object_name': 'FreshwaterFish'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'breeding_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aquainfo.FishBreedingType']", 'null': 'True', 'blank': 'True'}),
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'hardness_max': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hardness_min': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'origin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aquainfo.Origin']", 'null': 'True', 'blank': 'True'}),
            'ph_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'ph_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'preferred_area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aquainfo.FishTankRegion']", 'null': 'True', 'blank': 'True'}),
            'scientific_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'size_max': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'size_min': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '64'}),
            'temperament_family': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fishtemperament_family_set'", 'null': 'True', 'to': "orm['aquainfo.FishTemperament']"}),
            'temperament_others': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fishtemperament_others_set'", 'null': 'True', 'to': "orm['aquainfo.FishTemperament']"}),
            'temperature_max': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'temperature_min': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'aquainfo.freshwaterplant': {
            'Meta': {'ordering': "('common_name',)", 'object_name': 'FreshwaterPlant'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'growth_speed': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aquainfo.PlantGrowthSpeed']", 'null': 'True', 'blank': 'True'}),
            'hardness_max': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hardness_min': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lighting': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aquainfo.PlantLighting']", 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'origin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aquainfo.Origin']", 'null': 'True', 'blank': 'True'}),
            'ph_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'ph_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'placement': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aquainfo.PlantTankRegion']", 'null': 'True', 'blank': 'True'}),
            'propagation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aquainfo.PlantPropagationType']", 'null': 'True', 'blank': 'True'}),
            'scientific_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'size_max': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'size_min': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '64'}),
            'substrate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aquainfo.PlantSubstrate']", 'null': 'True', 'blank': 'True'}),
            'temperature_max': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'temperature_min': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'aquainfo.origin': {
            'Meta': {'object_name': 'Origin'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '64'})
        },
        'aquainfo.plantgrowthspeed': {
            'Meta': {'object_name': 'PlantGrowthSpeed'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '64'})
        },
        'aquainfo.plantlighting': {
            'Meta': {'object_name': 'PlantLighting'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '64'})
        },
        'aquainfo.plantpropagationtype': {
            'Meta': {'object_name': 'PlantPropagationType'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '64'})
        },
        'aquainfo.plantsubstrate': {
            'Meta': {'object_name': 'PlantSubstrate'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '64'})
        },
        'aquainfo.planttankregion': {
            'Meta': {'object_name': 'PlantTankRegion'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '64'})
        }
    }

    complete_apps = ['aquainfo']
