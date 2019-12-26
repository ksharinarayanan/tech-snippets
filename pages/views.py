#from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Blog

# Create your views here.
def home_view(request, *args, **kwargs):
    featured = Blog.objects.all().order_by('id').reverse()[:1]
    
    trending = Blog.objects.all().order_by('id').reverse()[:4]

    all_objects = Blog.objects.all().order_by('id').reverse()

    content = {
        'featured' : featured,
        'trending' : trending,
        'all_blogs' : all_objects,
    }

    return render(request, 'home/landingpage.html', content)

def about_view(request):
    return render(request, 'pages/about.html', {})

