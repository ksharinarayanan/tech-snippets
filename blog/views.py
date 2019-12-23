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
    
    content = {
        'blog' : obj,
    }
    return render(request, "blog/display.html", content)