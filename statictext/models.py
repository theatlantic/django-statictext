from django.db import models

__all__ = ["StaticText", "SingleStaticText"]


class StaticText(models.Model):
    """Stores a bit of rich text with a lookup slug and an enabled bool"""

    enabled = models.BooleanField(default=False, help_text="Display on Site")
    content = models.TextField(max_length=500, blank=True)
    url = models.URLField(name="URL", blank=True)
    slug = models.SlugField(db_index=True)

    class Meta:
        verbose_name = u'Text Snippet'
        verbose_name_plural = u'Text Snippets'


class StaticTextProxyManager(models.Manager):

    def get_object(self):
        # Make one row for the proxy class if it doesn't exist yet
        obj, _ = self.get_or_create(slug=self.model.proxy_slug)
        return obj


class SingleStaticText(StaticText):
    objects = StaticTextProxyManager()

    class Meta:
        abstract = True
