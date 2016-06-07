from django.contrib import admin
from django.contrib.sites.models import Site
from django.http import HttpResponseRedirect

from .forms import StaticTextForm

__all__ = ["SingleStaticTextAdmin", ]


class SingleStaticTextAdmin(admin.ModelAdmin):
    form = StaticTextForm

    # Make it a singleton item
    def get_actions(self, request):
        actions = super(SingleStaticTextAdmin, self).get_actions(request)
        actions.pop("delete_selected", None)
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def changelist_view(self, request, extra_context=None):
        """ Redirect the user to the only object in the admin. """
        try:
            site = self.model.proxy_site
        except AttributeError:
            site = Site.objects.get_current()

        obj, _ = self.model.objects.get_or_create(slug=self.model.proxy_slug, site=site)

        return HttpResponseRedirect('%s/' % obj.id)
