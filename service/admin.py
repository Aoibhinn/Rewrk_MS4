from django.contrib import admin
from .models import Service
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Service)
class ServiceAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('service_name',)}
    list_display = ('service_name', 'slug', 'status', 'price')
    search_fields = ['service_name', 'employee']
    list_filter = ('status', 'created_on')
    summernote_fields = ('description')