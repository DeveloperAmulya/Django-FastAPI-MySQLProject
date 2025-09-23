from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'published_at', 'created_at')
    list_filter = ('status', 'author')
    search_fields = ('title', 'body', 'excerpt')
    prepopulated_fields = {'slug' : ('title', )}
    date_hierarchy = 'published_at'
    ordering = ('-published_at',)
