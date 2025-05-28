from django.contrib import admin
from .models import ApiKey

@admin.register(ApiKey)
class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('key', 'created_at', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('key',)
