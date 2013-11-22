# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Deleting field 'StaticText.URL'
        db.delete_column('statictext_statictext', 'URL')

        # Adding field 'StaticText.url'
        db.add_column('statictext_statictext', 'url', self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Adding field 'StaticText.URL'
        db.add_column('statictext_statictext', 'URL', self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True), keep_default=False)

        # Deleting field 'StaticText.url'
        db.delete_column('statictext_statictext', 'url')
    
    
    models = {
        'sites.site': {
            'Meta': {'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'statictext.statictext': {
            'Meta': {'unique_together': "(('slug', 'site'),)", 'object_name': 'StaticText'},
            'content': ('django.db.models.fields.TextField', [], {'max_length': '500', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }
    
    complete_apps = ['statictext']
