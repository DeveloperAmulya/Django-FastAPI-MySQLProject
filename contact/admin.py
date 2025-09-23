from django.contrib import admin
from .models import Contact 

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'replied')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('replied',)
    readonly_fields = ('created_at',)
