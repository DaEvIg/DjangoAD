from django.contrib import admin
from safedelete.admin import SafeDeleteAdmin, SafeDeleteAdminFilter, highlight_deleted
from .models import Ad


class AdAdmin(SafeDeleteAdmin):
    list_display = (highlight_deleted, "highlight_deleted_field", "author", "title", "category", "text", "created_date", "published_date") + SafeDeleteAdmin.list_display
    list_filter = ("title", SafeDeleteAdminFilter,) + SafeDeleteAdmin.list_filter
    field_to_highlight = "id"

admin.site.register(Ad, AdAdmin)
AdAdmin.highlight_deleted_field.short_description = AdAdmin.field_to_highlight