from django.contrib import admin
from .models import *

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created_at'] # 커스터마이징 코드

admin.site.register(Post, PostAdmin)
