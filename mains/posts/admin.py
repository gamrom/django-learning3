from django.contrib import admin
from .models import *

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'photo', 'created_at'] # 커스터마이징 코드

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'content']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
