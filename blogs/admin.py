from django.contrib import admin
from .models import Category, Blog

class AdminBlog(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'category', 'status', 'is_featured')
    search_fields = ('id','title', 'category__category_name', 'status')
    list_editable = ('is_featured',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, AdminBlog)
