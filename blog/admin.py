from django.contrib import admin
from .models import Post, Comment

# A custom admin configuration for Posts
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    # This automatically fills in the slug field as you type the title!
    prepopulated_fields = {'slug': ('title',)}

# Simple registration for Comments
admin.site.register(Comment)