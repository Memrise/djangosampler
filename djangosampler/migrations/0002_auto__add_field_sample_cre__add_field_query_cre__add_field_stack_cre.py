# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Sample.cre'
        db.add_column('djangosampler_sample', 'cre', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now), keep_default=False)

        # Adding field 'Query.cre'
        db.add_column('djangosampler_query', 'cre', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now), keep_default=False)

        # Adding field 'Stack.cre'
        db.add_column('djangosampler_stack', 'cre', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Sample.cre'
        db.delete_column('djangosampler_sample', 'cre')

        # Deleting field 'Query.cre'
        db.delete_column('djangosampler_query', 'cre')

        # Deleting field 'Stack.cre'
        db.delete_column('djangosampler_stack', 'cre')


    models = {
        'djangosampler.query': {
            'Meta': {'object_name': 'Query'},
            'count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cre': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'hash': ('django.db.models.fields.CharField', [], {'max_length': '32', 'primary_key': 'True'}),
            'query': ('django.db.models.fields.TextField', [], {}),
            'query_type': ('django.db.models.fields.CharField', [], {'max_length': '32', 'db_index': 'True'}),
            'total_cost': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'total_duration': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        'djangosampler.sample': {
            'Meta': {'object_name': 'Sample'},
            'cost': ('django.db.models.fields.FloatField', [], {}),
            'cre': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'duration': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'params': ('django.db.models.fields.TextField', [], {}),
            'query': ('django.db.models.fields.TextField', [], {}),
            'stack': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['djangosampler.Stack']"})
        },
        'djangosampler.stack': {
            'Meta': {'object_name': 'Stack'},
            'count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cre': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'hash': ('django.db.models.fields.CharField', [], {'max_length': '32', 'primary_key': 'True'}),
            'query': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['djangosampler.Query']"}),
            'stack': ('django.db.models.fields.TextField', [], {}),
            'total_cost': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'total_duration': ('django.db.models.fields.FloatField', [], {'default': '0'})
        }
    }

    complete_apps = ['djangosampler']
