from django.shortcuts import render
from blogs.models import Blog


def home(request):
    posts = Blog.objects.filter(status="published")
    featured_post = Blog.objects.filter(status="published", is_featured=True)
    context = {
        'featured_post': featured_post,
        'posts': posts,
    }
    return render(request, 'home.html', context)
