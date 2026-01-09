from django.shortcuts import render
from blogs.models import Blog
from assignment.models import About, SocialMedia


def home(request):
    posts = Blog.objects.filter(status="published")
    featured_post = Blog.objects.filter(status="published", is_featured=True)
    try:
        about = About.objects.get()
    except:
        about = None  
      
    context = {
        'featured_post': featured_post,
        'posts': posts,
        'about': about,
    
    }
    return render(request, 'home.html', context)
