from django.shortcuts import  get_object_or_404, redirect, render
from .models import Blog, Category

# Create your views here.
def posts_by_category(request, category_id):
    # fetch the posts that belongs to the category with the id category_id
    posts = Blog.objects.filter(status="published", category = category_id)
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'posts_by_category.html', context)