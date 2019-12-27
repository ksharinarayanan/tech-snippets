#from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Blog

from comments.models import Comments

# Create your views here.
def home_view(request, *args, **kwargs):
    featured = Blog.objects.all().order_by('id').reverse()[:1]

    all_objects = Blog.objects.all().order_by('id').reverse()
    all_comments = Comments.objects.all()

    result = {}

    for comment in all_comments: 
        if comment.blog in result:
            result[comment.blog] += 1
        else:
            result[comment.blog] = 1
    result = sorted(result.items(), key=lambda kv: kv[1], reverse=True)

    

    result = dict(result)

    for blog in all_objects:
        if blog in result:
            continue;
        else:
            result[blog] = 0

    result = result[:4]
 

    content = {
        'featured' : featured,
        'trending' : result,
        'all_blogs' : all_objects,
    }

    return render(request, 'home/landingpage.html', content)

def about_view(request):
    return render(request, 'pages/about.html', {})

