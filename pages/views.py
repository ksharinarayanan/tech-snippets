#from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Blog

# Create your views here.
def home_view(request, *args, **kwargs):
    featured = Blog.objects.all().order_by('date').reverse()[:1]
    
    trending = Blog.objects.all().order_by('date').reverse()

    content = {
        'featured' : featured,
        'trending' : trending,
    }

    return render(request, 'home/landingpage.html', content)

