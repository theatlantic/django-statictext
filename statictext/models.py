from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager

__all__ = ["StaticText", "ProxySite",]


class ProxySite(object):
    """
    Use the ProxySite descriptor to lazy-evaluate site definitions. Useful
    during testing if the django_site table does not exist.
    """
    def __init__(self, **kwargs):
        try:
            self.site = Site.objects.get(**kwargs)
        except:
            self.site = None

    def __get__(self, object, value):
        return self.site

    def __set__(self, object, value):
        raise ValueError("Setting ProxySite after instantiation is not supported.")


class StaticText(models.Model):
    """Stores a bit of rich text with a lookup slug and an enabled bool"""

    enabled = models.BooleanField(default=False, help_text="Display on Site")
    content = models.TextField(max_length=500, blank=True)
    url = models.URLField("URL", blank=True)
    slug = models.SlugField(db_index=True)
    site = models.ForeignKey(Site)

    def __unicode__(self):
        """
        The unicode representation will contain the first fifty characters of
        the content followed by '(Disabled)' if the snippet is disabled.
        """
        truncated_content = (self.content[:50] + "...") if len(self.content) > 50 else self.content
        enabled = "" if self.enabled else " (Disabled)"

        return "\"%s\"%s" % (truncated_content, enabled)

    class Meta:
        verbose_name = u'Text Snippet'
        verbose_name_plural = u'Text Snippets'

        unique_together = (("slug", "site"),)
