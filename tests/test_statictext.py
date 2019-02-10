"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.contrib.sites.models import Site

from statictext.models import StaticText
from statictext.forms import StaticTextWithLayoutForm


class SimpleTest(TestCase):

    def test_statictext(self):
        """Very basic test for model and form."""

        form = StaticTextWithLayoutForm({
            'enabled': True,
            'content': 'loremipsum' * 10,
            'url': 'http://domain.com/url/',
            'layout': 'layout',
        })
        self.assertEqual(form.is_valid(), True)

        statx = form.save(commit=False)
        statx.site = Site.objects.create(domain='domain.com', name='Domain')
        statx.save()

        self.assertTrue('...' in str(statx))
