from django.contrib import admin
from services.models import File


class FileAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'is_active', 'uploaded_at']
    list_filter = ['is_active', 'uploaded_at']
    search_fields = ('user__email', 'title',)
    autocomplete_fields = ('user',)


admin.site.register(File, FileAdmin)
