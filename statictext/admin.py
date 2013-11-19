from django.contrib import admin
from django.http import HttpResponseRedirect

from .models import StaticText

__all__ = ["SingleStaticTextAdmin",]


class StaticTextAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': ('enabled', 'slug', 'content', 'URL',)
        }),
    )


class SingleStaticTextAdmin(admin.ModelAdmin):
    """
    This admin class is designed to be used with statictext.SingleStaticText.
    """

    fieldsets = (
        (None, {
            'fields': ('enabled', 'content', 'URL',)
        }),
    )


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
        destination = '%s/' % self.model.objects.get_object().id
        return HttpResponseRedirect(destination)
