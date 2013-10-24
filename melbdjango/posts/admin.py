from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'status']
    list_filter = ['status', 'created']

admin.site.register(Post, PostAdmin)
