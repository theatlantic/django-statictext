# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'StaticText'
        db.create_table('statictext_statictext', (
            ('content', self.gf('django.db.models.fields.TextField')(max_length=500, blank=True)),
            ('URL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
        ))
        db.send_create_signal('statictext', ['StaticText'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'StaticText'
        db.delete_table('statictext_statictext')
    
    
    models = {
        'statictext.statictext': {
            'Meta': {'object_name': 'StaticText'},
            'URL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'max_length': '500', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }
    
    complete_apps = ['statictext']
