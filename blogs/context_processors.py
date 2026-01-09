from blogs.models import Category
from assignment.models import SocialMedia
def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def get_social_links(request):
    social_links = SocialMedia.objects.all()
    return dict(social_links=social_links)