"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Service


@admin.register(Service)
class ServiceAdmin(SummernoteModelAdmin):
    """Services fields for display and filter"""

    prepopulated_fields = {'slug': ('service_name',)}
    list_display = ('service_name', 'slug', 'status', 'price')
    search_fields = ['service_name', 'employee']
    list_filter = ('status', 'created_on')
    summernote_fields = ('description')
