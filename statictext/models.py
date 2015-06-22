from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager

__all__ = ["StaticText", "ProxySite",]


class ProxySite(object):
    """
    Use the ProxySite descriptor to lazy-evaluate site definitions. Useful
    during testing if the django_site table does not exist.
    """
    _site = None

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __get__(self, instance, owner):
        if not self._site:
            try:
                self._site = Site.objects.get(**self.kwargs)
            except Site.DoesNotExist:
                pass

        return self._site

    def __set__(self, instance, value):
        raise ValueError("Setting ProxySite after instantiation is not supported.")


class StaticText(models.Model):
    """Stores a bit of rich text with a lookup slug and an enabled bool"""

    enabled = models.BooleanField(default=False, help_text="Display on Site")
    content = models.TextField(max_length=500, blank=True)
    url = models.URLField("URL", blank=True)
    slug = models.SlugField(db_index=True)
    site = models.ForeignKey(Site)
    layout = models.CharField(max_length=100, blank=True, default="")

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
