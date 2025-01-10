from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ('is_published',)
    list_display = ('title','author','created','is_published',)
    search_fields = ('title',)
    ordeing = ('-created',)
    