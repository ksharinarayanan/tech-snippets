from django.shortcuts import render

from .models import Blog
# Create your views here.
def blog_view(request):
    obj = Blog.objects.all().order_by('date').reverse()
    
    content = {
        'blogs' : obj,
    }

    return render(request, "blog/index.html", content)

def blog_detail_view(request, id):
    obj = Blog.objects.get(id=id)
    all_obj = Blog.objects.all().order_by('date').reverse()[:3]
    
    content = {
        'blog' : obj,
        'all_blogs' : all_obj,
    }
    return render(request, "blog/story.html", content)

def home_view(request, *args, **kwargs):
    #featured = Blog.objects.all().order_by('date').reverse()[:1]
    test = Blog.objects.get(id=2)
    
    #trending = Blog.objects.all().order_by('date').reverse()

    content = {
        """ 'featured' : featured,
        'trending' : trending, """
        'test' : test
    }

    return render(request, 'test.html', content)